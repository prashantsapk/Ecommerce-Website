"""
URL configuration for Ecommerce_Website_Main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views

urlpatterns = [
    path('',views.userhome,name="userhome"),
    path('pricing/',views.pricings,name="pricing"),
    path('jeans/',views.jeanss,name="jeans"),
    path('tshirts/',views.tshirtss,name="tshirtss"),
    path('sweaters/',views.sweaterss,name="sweaters"),
    path('jacketsandbagpacks/',views.jacketsandbagpackss,name="jacketsandbagpacks"),
    path('otheraccessories/',views.otheraccessoriess,name="otheraccessories"),
    path('login/',views.logins,name="login"),
    path('signup/',views.signups,name="signup"),

]
