from django.urls import path

from . import views 

urlpatterns = [
    path('email_comfirmation', views.email_confirmation),
]