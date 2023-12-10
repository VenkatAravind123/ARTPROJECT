from django.http import HttpResponse
from django.shortcuts import render



def home(request):
    return render(request,"index.html")
def paintings(request):
    return render(request,"paintings.html")
def sculptures(request):
    return render(request,"sculptures.html")
def artists(request):
    return render(request,"artists.html")
def about(request):
    return render(request,"about.html")
def home1(request):
    return render(request,"index.html")
def contact(request):
    return render(request,"contact.html")
def login(request):
    return render(request,"login.html")

def artistlogin(request):
    return render(request,"artistlogin.html")
def customerlogin(request):
    return render(request,"customerlogin.html")
def signin(request):
    return render(request,"signin.html")

