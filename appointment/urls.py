
from django.contrib import admin
from django.urls import path
from appointment.views.crud import *


urlpatterns = [
    path('',signup,name='signup'),
     path('login/',login,name='login'),
    
]
