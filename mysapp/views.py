from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def saludo(request):
    return render(request, "index.html")

def test(request):
    return render(request, "test.html")
