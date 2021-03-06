from django.db import models
from datetime import datetime
from realtors.models import Realtor
# Create your models here.

class Listing(models.Model):
    realtor = models.ForeignKey(Realtor,on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=80)
    city = models.CharField(max_length=80)
    county = models.CharField(max_length=80)
    address = models.CharField(max_length=80)
    description = models.TextField(max_length=400,blank=True)
    price = models.PositiveIntegerField()
    bedrooms = models.PositiveIntegerField()
    bathrooms = models.DecimalField(max_digits=2,decimal_places=1)
    garage = models.PositiveIntegerField(default=0)
    sqft = models.PositiveIntegerField()
    bedrooms = models.PositiveIntegerField()
    lot_size = models.DecimalField(max_digits=6,decimal_places=1)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/',default='NO IMAGE')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now,blank=True)

    def __str__(self):
        return self.title
