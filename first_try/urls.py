from django.urls import path
from django.http import HttpResponse
from .views import index, second

urlpatterns = [
    path('', index),
    path('second/', second)
]