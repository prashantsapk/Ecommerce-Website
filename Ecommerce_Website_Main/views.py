from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'Website/homepage.html')

def pricing(request):
    return HttpResponse("You are at pricing page")

def jeans(request):
    return HttpResponse("You are at jeans page")

def tshirts(request):
    return HttpResponse("You are at tshirts page")

def sweaters(request):
    return HttpResponse("You are at Sweaters page")

def jacketsandbagpacks(request):
    return HttpResponse("You are at Jacket and Bagpacks page")

def otheraccessories(request):
    return HttpResponse("You are at Acessories page")

