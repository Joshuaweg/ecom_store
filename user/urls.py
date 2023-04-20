from django.urls import path

from . import views 

urlpatterns = [
    path('user/login', views.login), 
    path('user/signup', views.sign_up)
]
