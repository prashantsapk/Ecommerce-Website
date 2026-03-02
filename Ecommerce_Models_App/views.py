from django.shortcuts import render
from django.http import HttpResponse
from .models import tshirts
from django.shortcuts import get_object_or_404
# Create your views here.

def userhome(request):
    return HttpResponse("This is user page")


def pricings(request):
    return render(request,"Website/pricing.html")

def jeanss(request):
    return render(request,"Website/jeans.html")

def tshirtss(request):
    a = tshirts.objects.all()
    return render(request,"Website/tshirts.html",{'a': a})

def sweaterss(request):
    return render(request,"Website/sweaters.html")

def jacketsandbagpackss(request):
    return render(request,"Website/jacketsandbagpacks.html")

def otheraccessoriess(request):
    return render(request,"Website/otheraccessories.html")

def logins(request):
    return render(request,"Website/login.html")

def signups(request):
    return render(request,"Website/signup.html")

def tshirtsdetails(request,tshirts_id):
    detailsoftshirts= get_object_or_404(tshirts,pk=tshirts_id)
    return render(request,'Website/tshirtsdetails.html',{'detailsoftshirts':detailsoftshirts})


