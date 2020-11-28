from django.db import models
import re
#-----------------------------
def remove_html_tags(text):
    """Remove html tags from a string"""
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)
#-----------------------------
# Create your models here.
class Sport(models.Model):
    Types = (
        ("Indoor", "Indoor"),
        ("Outdoor", "Outdoor")
    )
    name        =   models.CharField(max_length=1000)
    description =   models.TextField(blank=True)
    image       =   models.ImageField(blank=True)
    registration=   models.CharField(max_length=1000, help_text="recommended height 1000")
    howtoplay   =   models.TextField(blank=True)
    sporthead   =   models.CharField(max_length=1000)
    fees        =   models.IntegerField()
    door        =   models.CharField(max_length=7, choices=Types)

    def __str__(self):
        return remove_html_tags(self.name)

class Sportlist(models.Model):
    imageOne    =   models.ImageField(blank=True)
    imageTwo    =   models.ImageField(blank=True)
    imageThree  =   models.ImageField(blank=True)
    description =   models.TextField(blank=True)
    sports      =   models.ManyToManyField(Sport, related_name="sportsofsportlist", blank=True)

    def __str__(self):
        return "Sportslist"
