from django.db import models
from datetime import datetime

# Create your models here

class Realtor(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    description = models.TextField(max_length=400,blank=True)
    phone = models.PositiveIntegerField(blank=True,null=True)
    email = models.EmailField(max_length=40)
    is_mvp = models.BooleanField(default=False)
    hire_date = models.DateTimeField(default=datetime.now,blank=True)

    def __str__(self):
        return self.name
