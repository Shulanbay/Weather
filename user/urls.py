from django.conf.urls import url
from . import views

urlpatterns = [
    url('login/', views.user_login, name='login'),
    url('logout/', views.user_logout, name='logout'),
    url('register/', views.user_register, name='register'),
    url('facebook/', views.facebook, name='facebook'),
]
