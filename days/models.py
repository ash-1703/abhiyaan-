from django.db import models
import re
# Create your models here.

#-----------------------------
def remove_html_tags(text):
    """Remove html tags from a string"""
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)
#-----------------------------
class Event(models.Model):
    name           =  models.CharField(max_length=1000)
    image          =  models.ImageField(upload_to='images', blank=True)
    description    =  models.TextField(blank=True)
    eventhead      =  models.CharField(max_length=1000)
    rules          =  models.TextField(blank=True)    
    registrationform= models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return remove_html_tags(self.name)

class Day(models.Model):
    name        =  models.CharField(max_length=1000)
    imageOne    =  models.ImageField(upload_to='images', blank=True)
    imageTwo    =  models.ImageField(upload_to='images', blank=True)
    imageThree  =  models.ImageField(upload_to='images', blank=True)
    description =  models.TextField(blank=True)
    events      =  models.ManyToManyField(Event, blank=True, related_name="eventsofday")

    def __str__(self):
        return remove_html_tags(self.name)
    

class Days(models.Model):
    imageOne   =  models.ImageField(upload_to='images', blank=True)
    imageTwo   =  models.ImageField(upload_to='images', blank=True)
    imageThree =  models.ImageField(upload_to='images', blank=True)
    description=  models.TextField(blank=True)
    day        =  models.ManyToManyField(Day, blank=True, related_name="dayofdays")

    def __str__(self):
        return 'Days'