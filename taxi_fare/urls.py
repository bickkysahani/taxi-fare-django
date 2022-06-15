from django.urls import path
from .views import *

urlpatterns = [
    path('index/',index,name='index'),
    #path('calculate_fare/',calculate,name='calculate_fare'),
]