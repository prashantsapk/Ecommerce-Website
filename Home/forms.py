from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


class signupform(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['first_name','last_name','email','password1','password2']
        
class loginform(AuthenticationForm):

    class Meta:
        model = User
        fields = '__all__'
