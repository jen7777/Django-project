from django.shortcuts import render
from django.http import HttpResponse
from .models import Departments
# Create your views here.
def index(request):
    return render(request,'home.html')      #or return HttpResponse("Home")
def about(request):
    return render(request,'about.html')

def booking(request):
    return render(request,'booking.html')

def doctors(request):
    return render(request,'doctors.html')

def contact(request):
    return render(request,'contact.html')

def departments(request):
    dict_dept={
        'dept': Departments.objects.all()         #pull all objects from class dept
    }
    return render(request,'departments.html',dict_dept)