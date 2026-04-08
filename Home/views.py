from django.shortcuts import render,redirect
from .models import jeanmodel,tshirtmodel,sweatermodel,otheraccessoriesmodel,bagpackmodel
from .forms import signupform,loginform
from django.contrib.auth import login


# Create your views here.

def homepageview(request):

    return render(request,'homepage.html')
   
def tshirtview(request):
    

    return render(request,'tshirt.html')

def jeanview(request):
    obj= jeanmodel.objects.all()
    
    return render(request,'jean.html',{'obj':obj})
   
def sweaterview(request):

    return render(request,'sweater.html')
   
def bagpackview(request):

    return render(request,'bagpack.html')
   
def otheraccessoriesview(request):

    return render(request,'otheraccessories.html')
   
def pricingview(request):

    return render(request,'pricing.html')
   
def signupview(request):
    if request.method=="POST":
        signupobj = signupform(request.POST)
        if signupobj.is_valid():
            user = signupobj.save()
    else:
        signupobj = signupform()

    return render(request,'signup.html',{'signupobj':signupobj})
   
def loginview(request):

   if request.method=="POST":
        loginobj = loginform(request.POST)
        if loginobj.is_valid():
            user = loginobj
            login(user,request)
            redirect('homepage')
   else:
        loginobj = loginform()
        return render(request,'login.html',{'loginobj':loginobj})
   