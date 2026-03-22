from django.urls import path,include
from . import views
from .views import homepageview,jeanview,sweaterview,tshirtview,bagpackview,otheraccessoriesview,pricingview,signupview,loginview



urlpatterns = [
    
    path('',views.homepageview,name='homepage'),
    path('pricing/',views.pricingview,name='pricing'),
    path('jean/',views.jeanview,name='jean'),
    path('sweater/',views.sweaterview,name='sweater'),
    path('tshirt/',views.tshirtview,name='tshirt'),
    path('bagpack/',views.bagpackview,name='bagpack'),
    path('otheraccessories/',views.otheraccessoriesview,name='otheraccessories'),
    path('signup/',views.signupview,name='signup'),
    path('login/',views.loginview,name='login'),
    
]

    
