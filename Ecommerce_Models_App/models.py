from django.db import models

# Create your models here.
class jeans(models.Model):
    Name= models.CharField(max_length=100)
    Description= models.TextField(max_length=100)
    Image=models.ImageField(upload_to='Ecommerce_Models_App')
    Price=models.IntegerField()
    Type= models.CharField(max_length=15)

    def __str__(self):
        return self.Name

    
    


class sweaters(models.Model):
    Name= models.CharField(max_length=15)
    Description= models.CharField(max_length=100)
    Image=models.ImageField(upload_to='Ecommerce_Models_App')
    Price=models.IntegerField()
    Type= models.CharField(max_length=15)

    def __str__(self):
        return self.Name
        

class jackets(models.Model):
    Name= models.CharField(max_length=15)
    Description= models.TextField(max_length=100)
    Image=models.ImageField(upload_to='Ecommerce_Models_App')
    Price=models.IntegerField()
    Type= models.CharField(max_length=15)

    def __str__(self):
        return self.Name
        


class tshirts(models.Model):
    Name= models.CharField(max_length=15)
    Description= models.TextField(max_length=100)
    Image=models.ImageField(upload_to='Ecommerce_Models_App')
    Price=models.IntegerField()
    Type= models.CharField(max_length=15)

    def __str__(self):
        return self.Name
        

class bagpacks(models.Model):
    Name= models.CharField(max_length=15)
    Description= models.TextField(max_length=100)
    Image=models.ImageField(upload_to='Ecommerce_Models_App')
    Price=models.IntegerField()
    Type= models.CharField(max_length=15)

    def __str__(self):
        return self.Name
        


class otheraccessories(models.Model):
    Name= models.CharField(max_length=15)
    Description= models.TextField(max_length=100)
    Image=models.ImageField(upload_to='Ecommerce_Models_App')
    Price=models.IntegerField()
    Type= models.CharField(max_length=15)

    def __str__(self):
        return self.Name
        

    