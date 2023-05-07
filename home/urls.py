from django.urls import path

from . import views 

urlpatterns = [
    path('home', views.home),
    path('accounts/signup',views.signup),
     path('test',views.test_layout)
]