from django.db import models


# Create your models here.

class RestaurantPhotos(models.Model):
    img = models.ImageField(upload_to='picture')
    value = models.CharField(max_length=25)
