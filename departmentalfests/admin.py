from django.contrib import admin
from .models import *

class GeneralAdmin(admin.ModelAdmin):
    class Media:
        css = {
            "all": ("css/main.css",)
        }
        js = ("js/richtext.js",)
# Register your models here.
admin.site.register(DepartmentalFest, GeneralAdmin)
admin.site.register(Department, GeneralAdmin)
admin.site.register(Event, GeneralAdmin)