
from django.urls import path

from . import views

urlpatterns = [
    path('', views.step_counter, name='step_counter'),
]

