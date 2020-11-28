from django.contrib import admin
from .models import *

class GeneralAdmin(admin.ModelAdmin):
    class Media:
        css = {
            "all": ("css/main.css",)
        }
        js = ("js/richtext.js",)
# Register your models here.
admin.site.register(Sport, GeneralAdmin)
admin.site.register(Sportlist, GeneralAdmin)