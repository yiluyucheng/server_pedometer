
from django.urls import path
from django.urls import include, re_path

from . import views

urlpatterns = [
    path('', views.step_counter, name='step_counter'),
    re_path(r'^chart/$', views.ChartView.as_view(), name='chart_info'),
    re_path(r'^index/$', views.IndexView.as_view(), name='index_view'),
]

