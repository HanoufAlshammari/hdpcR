from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def Hanouf(request):
    return render(request,'Hanouf.html')
def Contact(request):
    return render(request,'Contact.html')
