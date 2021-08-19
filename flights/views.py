from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Flight
# Create your views here.


def home(request):
  return render (request,'flights/home.html')


def index(request):
  return render(request,'flights/index.html',{
    'flights' : Flight.objects.all()
  })

def show(request,flight_id):
  return render(request,'flights/show.html',{
    'flight': Flight.objects.get(pk=flight_id)
  })
