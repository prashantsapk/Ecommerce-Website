from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'Website/homepage.html')

def pricing(request):
    return render(request,"Website/pricing.html")

def jeans(request):
    return render(request,"Website/jeans.html")

def tshirts(request):
    return render(request,"Website/tshirts.html")

def sweaters(request):
    return render(request,"Website/sweaters.html")

def jacketsandbagpacks(request):
    return render(request,"Website/jacketsandbagpacks.html")

def otheraccessories(request):
    return render(request,"Website/otheraccessories.html")

def login(request):
    return render(request,"Website/login.html")

def signup(request):
    return render(request,"Website/signup.html")




