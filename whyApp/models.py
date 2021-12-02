from django.db import models


# Create your models here.


class why(models.Model):
    # objects = all()
    # objects = None
    num = models.IntegerField()
    title = models.CharField(max_length=30)
    quotes = models.TextField(max_length=250)
    colour = models.CharField(max_length=20)

