from django.shortcuts import render
from django.http import HttpResponse
from . import models


# Create your views here.
def visualization(request):
    return render(request, 'uav/index.html')
