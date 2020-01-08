from django.http import HttpResponse
from django.shortcuts import render, redirect
# from .models import Myspot


# Create your views here.
def index(request):
    return render(request, 'home.html')


