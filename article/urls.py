from django.conf.urls import url
from django.conf.urls import *
from django.urls import path, include
from . import views


urlpatterns = [
    path('1', views.basic_one),
    path('articles/all', views.articles),
]
