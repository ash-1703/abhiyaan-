from django.shortcuts import render
from .models import *
from departmentalfests.models import *
#-----------------------------------------------------------
departmentalfests=DepartmentalFest.objects.all()
#-----------------------------------------------------------
# Create your views here.
def index(request):
    days=Days.objects.all()[0]
    day=Day.objects.all()
    departments=Department.objects.all()

    return render(request, "days/index.html", {
        "days": days,
        "day":day,
        "departments": departments,
        "sports":["Kabaddi", "Kho-Kho", "Cricket", "Batminton"]
    })

def day(request, day):
    oday=Day.objects.all()
    days=Days.objects.all()
    tday=Day.objects.get(name=day)
    events=Event.objects.all()
    departments=Department.objects.all()

    return render(request, "days/day.html", {
        "days": days,
        "day": oday,
        "tday":tday,
        "events": events,
        "departments": departments,
        "sports":["Kabaddi", "Kho-Kho", "Cricket", "Batminton"]
    })

def event(request, day, event):
    departments=Department.objects.all()
    days=Days.objects.all()[0]
    oday=Day.objects.all()
    tday=Day.objects.get(name=day)
    events=Event.objects.all()
    tevent=Day.objects.get(name=day).events.get(name=event)
    
    return render(request, "home/event.html", {
        "days": days,
        "day": oday,
        "tday": tday,
        "events": events,
        "event": tevent,
        "department": departments,
        "sports":["Kabaddi", "Kho-Kho", "Cricket", "Batminton"]
    })