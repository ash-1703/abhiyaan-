from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "maineventsdaytwo/index.html", {
        "days": ["Clan", "Corporate", "Traditional"],
        "departmentalfests": ["CSE", "IT", "EXTC", "ME", "CE"],
        "sports":["Kabaddi", "Kho-Kho", "Cricket", "Batminton"]
    })

def maineventsdaytwo(request):
    return render(request, "maineventsdaytwo/maineventsdaytwo.html", {
        "maineventsdaytwo":"Name of Main Events Day Two"
    })