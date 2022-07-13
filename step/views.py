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
        session_list = Session.objects.all().order_by('-ids')
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
        try:
            req = json.loads(request.body)
            step = req['Step']
            pain = req['Pain']
            ids = req['ids']
        except:
            ids = request.POST['ids']
            step = request.POST['Step']
            pain = request.POST['Pain']
        feedback = feed_back(int(step), int(pain))
        add_session = Session(ids=ids, step=step, pain=pain)
        add_session.save()
        return JsonResponse({"feedback": feedback,}) 
    form = StepForm()
    return render(request, 'step_count.html', {'form': form,})
 