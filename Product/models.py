
from django.db import models


# Create your models here.

class Racket(models.Model):
    name_seller = models.TextField(blank=False)
    address = models.TextField()
    name_bat = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='images/', blank=False)
    # photo = models.FileField(upload_to='pics/')
    desc = models.TextField(max_length=500)
    email = models.TextField()
    model_no = models.TextField()
    price = models.IntegerField()
    date_make = models.DateField()
    username = models.TextField()
