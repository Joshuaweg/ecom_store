'''
The user view is for handling when the user wants to login into their accout,
or if a new user wants to sign up.
Based on the needs of the user, they will be routed from the user view 
to the approiate webpage. 
'''
from django.shortcuts import render

# route to the Login page
def login(request):
    return render(request,'user/login.html')
# route to sign up page
def sign_up(request):
    return render(request,'user/register.html')