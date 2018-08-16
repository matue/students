from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    path('', GroupList,  name='GroupList'),
    path('group/<slug:group>', StudentList, name='StudentList')
]
