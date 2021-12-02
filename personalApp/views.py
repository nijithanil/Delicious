from django.http import HttpResponse
from django.shortcuts import render
# from .models import why
from .models import place


# Create your views here.

#
# def fun1(request):
#     obj1 = why.objects.all()
#     return render(request, 'index.html', {'whychooses': obj1})


def fun2(request):
    obj2 = place.objects.all()
    return render(request, 'index.html', {'values': obj2})


def result(request):
    number1 = int(request.POST['num1'])
    number2 = int(request.POST['num2'])
    sum = number1 + number2

    return render(request, 'result.html', {'value': sum})
