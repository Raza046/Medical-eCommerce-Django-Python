from django.db import models
from django.contrib.auth.models import User
from products.models import Products
# Create your models here.


class CartItems(models.Model):


    user = models.ForeignKey(User,on_delete="CASCADE",null=True)
    prod = models.ForeignKey(Products,on_delete="CASCADE",null=True,blank=True)
    quantity = models.IntegerField(default=1)
    total = models.DecimalField(max_digits=100,decimal_places=2,default=0.00)
    timestamp= models.DateTimeField(auto_now_add=True,auto_now=False)
    active= models.BooleanField(default=True)
    


class myCart(models.Model):

    user = models.ForeignKey(User,on_delete="CASCADE",null=True)
    items = models.ManyToManyField(CartItems,null=True,blank=True)
    prod = models.ManyToManyField(Products,null=True, blank=True)
    timestamp= models.DateTimeField(auto_now_add=True,auto_now=False)
    active= models.BooleanField(default=True)
    subtotal = models.FloatField(null=True)
    
