from django.shortcuts import render
from days.models import *
from .models import *

#---------------------------------------------------

#---------------------------------------------------

# Create your views here.
def index(request):
    days=Days.objects.all()[0]
    day=Day.objects.all()
    departmentalfests=DepartmentalFest.objects.all()[0]
    departments=Department.objects.all()
    events=Event.objects.all()
    return render(request, "departmentalfests/index.html", {
        "days": days,
        "day":day,
        "departments": departments,
        "departmentalfests": departmentalfests,
        "sports":["Kabaddi", "Kho-Kho", "Cricket", "Batminton"]
    }) 

def department(request, department):
    days=Days.objects.all()[0]
    day=Day.objects.all()
    departmentalfests=DepartmentalFest.objects.all()[0]
    departments=Department.objects.all()
    events=Event.objects.all()
    tdepartment=Department.objects.get(name=department)
    return render(request, "departmentalfests/department.html", {
        "days": days,
        "day": day,
        "departments": departments,
        "tdepartment": tdepartment,
        "events": events,
        "departmentalfests": departmentalfests,
        "sports":["Kabaddi", "Kho-Kho", "Cricket", "Batminton"]
    })

def event(request, department, event):
    tdepartment=Department.objects.get(name=department)
    tevent=Department.objects.get(name=department).events.get(name=event)
    days=Days.objects.all()[0]
    day=Day.objects.all()
    departmentalfests=DepartmentalFest.objects.all()[0]
    departments=Department.objects.all()
    events=Event.objects.all()

    return render(request, "home/event.html", {
        "days": days,
        "day": day,
        "events": events,
        "event": tevent,
        "department": departments,
        "tdepartment": tdepartment,
        "sports":["Kabaddi", "Kho-Kho", "Cricket", "Batminton"]
    })