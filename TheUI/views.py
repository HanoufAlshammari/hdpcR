from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def home(request):
    return render(request,'home.html')
def Home2(request):
    return render(request,'Home2.html')
