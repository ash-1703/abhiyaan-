from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    sportlist=Sportlist.objects.all()[0]
    sports=Sport.objects.all()
    isports=Sport.objects.filter(door="Indoor")
    osports=Sport.objects.filter(door="Outdoor")
    print(isports)
    print(osports)
    return render(request, "sports/index.html", {
        "days": ["Clan", "Corporate", "Traditional"],
        "departmentalfests": ["CSE", "IT", "EXTC", "ME", "CE"],
        "sports": sports,
        "isports": isports,
        "osports": osports,
        "sportlist":sportlist
        
    })

def sport(request, sport):
    sportlist=Sportlist.objects.all()[0]
    return render(request, "sports/sport.html", {
        "sport":[sportlist],
        "days": ["Clan", "Corporate", "Traditional"],
        "departmentalfests": ["CSE", "IT", "EXTC", "ME", "CE"],
        "sports":["Kabaddi", "Kho-Kho", "Cricket", "Batminton"]
    })