from django.shortcuts import render
from .models import jeanmodel,tshirtmodel,sweatermodel,otheraccessoriesmodel,bagpackmodel


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
   