"""
Definition of urls for ecom_store.
"""

from datetime import datetime
from django.urls import path, include
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from app import forms, views

# from home import views

# from products import views # No views yet

urlpatterns = [
   # path('/', include('home.urls')), #  <- Troy did not make this
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
    path('', include('home.urls')), # <- Troy added this 
    path('', include('products.urls')), # <- Troy Created this
    path('',include('orders.urls')),
    path('',include('credit_cards.urls')),
    path('', lambda req: redirect('/home')),
]
