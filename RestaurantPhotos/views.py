from django.http import HttpResponse
from django.shortcuts import render
from .models import RestaurantPhotos


# Create your views here.

def RestaurantPhotosfun(request):
    obj3 = RestaurantPhotos.objects.all()
    return render(request, 'index.html', {'photos': obj3})

