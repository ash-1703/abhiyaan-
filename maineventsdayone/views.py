from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    d=D.objects.all()
    
    return render(request, "maineventsdayone/index.html", {
        "d": d,
        "days": ["Clan", "Corporate", "Traditional"],
        "departmentalfests": ["CSE", "IT", "EXTC", "ME", "CE"],
        "sports":["Kabaddi", "Kho-Kho", "Cricket", "Batminton"]
    })

def maineventsdayone(request):
    return render(request, "maineventsdayone/maineventsdayone.html", {
        "maineventsdayone":"Name Of Events"
    })