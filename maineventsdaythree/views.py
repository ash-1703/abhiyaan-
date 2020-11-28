from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "maineventsdaythree/index.html", {
        "days": ["Clan", "Corporate", "Traditional"],
        "departmentalfests": ["CSE", "IT", "EXTC", "ME", "CE"],
        "sports":["Kabaddi", "Kho-Kho", "Cricket", "Batminton"]
    })

def maineventsdaythree(request):
    return render(request, "maineventsdaythree/maineventsdaythree.html", {
        "maineventsdaythree":"Name Of Events"
    })