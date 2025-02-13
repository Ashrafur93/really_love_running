from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

class HomeList:
    template_name = "home/index.html"

def home(request):
    return render(
        request,
        "home/index.html",
    )