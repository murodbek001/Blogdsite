from django.urls import path
from django.shortcuts import render

def index(request):
    return render(request,"main/index.html")

def about(request):
    return render(request,"main/about.html")

def services(request):
    return render(request,"main/services.html")
    
def contact(request):
    if request.method == "POST":
        print(request.POST)
    return render(request,"main/contact.html")