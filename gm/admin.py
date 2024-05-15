from django.contrib import admin
from .models import contact

# Register your models here.
class contactAdmin(admin.ModelAdmin):
    list_display=['name','email','Contactno','Requirement']
    search_fields=['name','email','Contactno']
    list_per_page=6
admin.site.register(contact,contactAdmin)