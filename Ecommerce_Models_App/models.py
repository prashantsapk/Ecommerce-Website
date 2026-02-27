from django.db import models

# Create your models here.
class jeans(models.Model):
    Name= models.CharField(max_length=100)
    Description= models.TextField(max_length=100)
    Price=models.IntegerField()
    Type= models.CharField(max_length=15)


class sweaters(models.Model):
    Name= models.CharField(max_length=15)
    Description= models.CharField(max_length=100)
    Price=models.IntegerField()
    Type= models.CharField(max_length=15)

class jackets(models.Model):
    Name= models.CharField(max_length=15)
    Description= models.TextField(max_length=100)
    Price=models.IntegerField()
    Type= models.CharField(max_length=15)


class tshirts(models.Model):
    Name= models.CharField(max_length=15)
    Description= models.TextField(max_length=100)
    Price=models.IntegerField()
    Type= models.CharField(max_length=15)

class bagpacks(models.Model):
    Name= models.CharField(max_length=15)
    Description= models.TextField(max_length=100)
    Price=models.IntegerField()
    Type= models.CharField(max_length=15)


class otheraccessories(models.Model):
    Name= models.CharField(max_length=15)
    Description= models.TextField(max_length=100)
    Price=models.IntegerField(max_length=5)
    Type= models.CharField(max_length=15)