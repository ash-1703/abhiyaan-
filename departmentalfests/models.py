from django.db import models
import re
#-----------------------------
def remove_html_tags(text):
    """Remove html tags from a string"""
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)
#-----------------------------
# Create your models here.
class Event(models.Model):
    name           =  models.CharField(max_length=1000)
    image          =  models.ImageField(upload_to='images', blank=True)
    description    =  models.TextField(blank=True)
    eventhead      =  models.CharField(max_length=1000)
    rules          =  models.TextField(blank=True)
    registrationform= models.CharField(max_length=1000, blank=True)


    def __str__(self):
        return remove_html_tags(self.name)
    
class Department(models.Model):
    name        =   models.CharField(max_length=1000)
    description =   models.TextField(blank=True)
    imageOne    =   models.ImageField(blank=True)
    imageTwo    =   models.ImageField(blank=True)
    imageThree  =   models.ImageField(blank=True)
    events      =   models.ManyToManyField(Event, related_name="eventofdepartment", blank=True)

    def __str__(self):
        return remove_html_tags(self.name)

class DepartmentalFest(models.Model):
    imageOne    =   models.ImageField(blank=True)
    imageTwo    =   models.ImageField(blank=True)
    imageThree  =   models.ImageField(blank=True)
    description =   models.TextField(blank=True)
    department  =   models.ManyToManyField(Department, related_name="departmentofdepartmentalfests", blank=True)

    def __str__(self):
        return "Departmentalfest"
