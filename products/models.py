from django.db import models


class Products(models.Model):

    name = models.CharField(max_length=50)
    price = models.PositiveIntegerField() 
    image = models.ImageField(upload_to='static')
    descriptions = models.CharField(max_length=500)
    slug = models.SlugField(unique=True)
    quantity = models.PositiveIntegerField(default=1)

    def __unicode__(self):

        return self.title

