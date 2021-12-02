from django.http import HttpResponse
from django.shortcuts import render
from .models import why


# Create your views here.


def fun1(request):
    obj1 = why.objects.all()
    return render(request, 'index.html', {'whychooses': obj1})

