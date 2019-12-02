
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),  #the path for our index view
    path('/<int:city_id>',views.citywiki,name='citywiki'),


]