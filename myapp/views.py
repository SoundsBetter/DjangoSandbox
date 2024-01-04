from django.shortcuts import render

from myapp.models import Consumer, ServiceProvider


def index(request):
    return render(request, "myapp/index.html")
