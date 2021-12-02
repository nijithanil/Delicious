from django.urls import path
from . import views

urlpatterns = [
    # path('', views.fun1, name='fun1'),
    path('', views.fun2, name='fun2'),
    path('add', views.result, name='add')
]
