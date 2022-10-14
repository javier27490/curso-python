from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def saludar(request):

    context = {}

    return render(request, 'AppCoder/index.html', context)
