from django.db import models
from django.contrib.auth.models import AbstractUser #gpt

# Create your models here.

class jeanmodel(models.Model):
    Type = models.CharField(max_length=50)
    Price = models.CharField(max_length=10)
    Image = models.ImageField(upload_to='jeans/')

    def __str__(self):
        return self.Type
    

class tshirtmodel(models.Model):
    Type = models.CharField(max_length=50)
    Price = models.CharField(max_length=10)
    Image = models.ImageField(upload_to='tshirts/')

    def __str__(self):
        return self.Type
    
    

class sweatermodel(models.Model):
    Type = models.CharField(max_length=50)
    Price = models.CharField(max_length=10)
    Image = models.ImageField(upload_to='sweaters/')

    def __str__(self):
        return self.Type
    
    

class bagpackmodel(models.Model):
    Type = models.CharField(max_length=50)
    Price = models.CharField(max_length=10)
    Image = models.ImageField(upload_to='bagpacks/')

    def __str__(self):
        return self.Type
    
    

class otheraccessoriesmodel(models.Model):
    Type = models.CharField(max_length=50)
    Price = models.CharField(max_length=10)
    Image = models.ImageField(upload_to='otheraccessories/')

    def __str__(self):
        return self.Type
    
    
