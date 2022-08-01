from django.shortcuts import render
from .forms import *
import json

from django.http import HttpResponse,JsonResponse
from .models import *
from django.core.paginator import Paginator


def feed_back(steps, pain):
    if pain < 30:
        words = "You felt good!"
        steps *= 1.1 
    elif pain < 70:
        words = "You felt a bit tired!"
        steps *= 0.9
    else:
        words = 'You were exhausted!'
        steps *= 0.5
    return(words + " Next time try to walk " + str(int(steps)) + " steps.")
    
    
    
def homeview(request, glist=None):
    # display table and seperate pages    
    if glist is None:
        session_list = Session.objects.all().order_by('-date', '-end')
    else:
        session_list = glist
    if session_list:
        paginator = Paginator(session_list, 10)
        page = request.GET.get('page')
        page_obj = paginator.get_page(page)
        return render(request, 'home.html',
                      {'page_obj': page_obj, 'paginator': paginator,
                       'is_paginated': True,})
    else:
        return render(request, 'home.html')    
    
    
def step_counter(request):    
    if request.method == 'POST':
        var = ['ids', 'Date', 'Step', 'Distance', 'Pain', 'Start', 'End', 'Height', 'Weight', 'Sex', 'Age']
        try:
            req = json.loads(request.body)
        except:
            req = dict()
            for i in var:
                req[i] = request.POST[i]            
        feedback = feed_back(int(req['Step']), int(req['Pain']))
        add_session = Session(ids=req['ids'], step=req['Step'], pain=req['Pain'], date=req['Date'], 
            distance=req['Distance'], start=req['Start'], end=req['End'], height=req['Height'],
            weight=req['Weight'], sex=req['Sex'], age=req['Age'])
        add_session.save()
        return JsonResponse({"feedback": feedback,}) 
    form = StepForm()
    return render(request, 'step_count.html', {'form': form,})
 
 
 
 ######################################################################    

# Create your views here.

from random import randrange

from rest_framework.views import APIView

from pyecharts.charts import Bar, Line
from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.globals import CurrentConfig
from jinja2 import Environment, FileSystemLoader
CurrentConfig.GLOBAL_ENV = Environment(loader=FileSystemLoader("./step/templates"))


# Create your views here.
def response_as_json(data):
    json_str = json.dumps(data)
    response = HttpResponse(
        json_str,
        content_type="application/json",
    )
    response["Access-Control-Allow-Origin"] = "*"
    return response


def json_response(data, code=200):
    data = {
        "code": code,
        "msg": "success",
        "data": data,
    }
    return response_as_json(data)


def json_error(error_string="error", code=500, **kwargs):
    data = {
        "code": code,
        "msg": error_string,
        "data": {}
    }
    data.update(kwargs)
    return response_as_json(data)


JsonResponse = json_response
JsonError = json_error

    
def bar_chart(indata) -> Bar:
    
    bar = (
        Bar()
        .add_xaxis(indata['date'])
        .add_yaxis("Step", indata['step'], yaxis_index=0, itemstyle_opts=opts.ItemStyleOpts(color='gray'))
        .extend_axis(
            yaxis=opts.AxisOpts(
                name="Pain",
                type_="value",
                min_=0,
                max_=100,
                position="right",
                axisline_opts=opts.AxisLineOpts(
                linestyle_opts=opts.LineStyleOpts(color='red')
                )
            )
        )
        .set_global_opts(
            xaxis_opts=opts.AxisOpts(name='Date', name_location='middle', name_gap=30, name_textstyle_opts=opts.TextStyleOpts(font_size = 18)),
            yaxis_opts=opts.AxisOpts(name='Steps by day', name_location='middle', name_gap=40, name_textstyle_opts=opts.TextStyleOpts(font_size = 14)))
               
    )
         
    line = (
        Bar()
        .add_xaxis(indata['date'])
        .add_yaxis("Pain", indata['pain'], yaxis_index=1, itemstyle_opts=opts.ItemStyleOpts(color='red'))
         
    )       

    return bar.overlap(line).dump_options_with_quotes()
            

class ChartView(APIView):
    def get(self, request, *args, **kwargs):
        #person = 'aid29903cc9-55ff-4ec7-a266-ae205c57f014'
        person = request.GET['person']
        session_list = Session.objects.all().order_by('-date', '-end').reverse()
        session_list = session_list.filter(ids=person)[:15].values('date', 'step', 'pain')
        n_date = []
        n_step = []
        n_pain = []
        pre = 'Fake-initial'
        for d in session_list:
            if pre == d['date']:
                n_step[-1] += int(d['step'])
                n_step[-1] = max(n_step[-1], int(d['pain']))
            else:
                n_date.append(d['date'])
                n_step.append(int(d['step']))
                n_pain.append(int(d['pain']))
                pre = d['date']
        d_step = {'ids': person, 'date':n_date, 'step':n_step, 'pain':n_pain}    
        return JsonResponse(json.loads(bar_chart(d_step)))

class IndexView(APIView):
    def get(self, request, *args, **kwargs):
        person = request.GET['person']
        return render(request, 'index.html', {'ids': person,})
