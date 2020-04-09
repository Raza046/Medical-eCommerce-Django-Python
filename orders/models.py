from django.db import models
from django.contrib.auth.models import User
from carts.models import myCart


country_choices = {

    ('P','Pakistan'),
    ('A','Australia'),
    ('U','USA'),
    ('NZ','New Zealand'),
    ('T','Turkey'),
    ('D','Dubai'),
}




class Order(models.Model):


    user = models.ForeignKey(User,on_delete="CASCADE")
    cart = models.OneToOneField(myCart,on_delete="CASCADE",null=True)
    fname = models.CharField(max_length=100, null=True)
    lname = models.CharField(max_length=100,null=True)
    email = models.EmailField(max_length=50,null=True)
    address = models.CharField(max_length=100,null=True)
    PostalCode = models.IntegerField(null=True)
    Contact = models.IntegerField(null=True)
    country = models.CharField(max_length=100,choices=country_choices,null=True)
#   status = models.CharField(choices=status,max_length=10,null=True)
    timestamp= models.DateTimeField(auto_now_add=True,auto_now=False,null=True)
    active= models.BooleanField(default=True,null=True)


