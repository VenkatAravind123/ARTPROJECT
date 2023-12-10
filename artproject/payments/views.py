from django.shortcuts import render
from . models import *



# Create your views here.


def payindex(request):
    return render(request, 'payindex.html')
