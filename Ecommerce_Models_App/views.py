from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def userhome(request):
    return HttpResponse("This is user page")
