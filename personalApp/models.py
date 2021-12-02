from django.db import models


# Create your models here.

#
# class why(models.Model):
#     num = models.IntegerField()
#     title = models.CharField(max_length=30)
#     quotes = models.TextField(max_length=250)
#     colour = models.CharField(max_length=20)
#

class place(models.Model):
    img = models.ImageField(upload_to='picture')
    name = models.CharField(max_length=20)
    position = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
