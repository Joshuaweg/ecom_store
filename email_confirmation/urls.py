from django.urls import path

from . import views 

urlpatterns = [
    path('email_confirmation', views.email_confirmation),
]