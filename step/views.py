from django.shortcuts import render
from .forms import *
# Create your views here.

from django.http import HttpResponse


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
    
    
    
def step_counter(request):
    form = StepForm()
    if request.method == 'POST':
        step = request.POST['Step']
        pain = request.POST['Pain']
        feedback = feed_back(int(step), int(pain))
        return render(request, 'step_display.html', {'feedback': feedback,})
    return render(request, 'step_count.html', {'form': form,})
