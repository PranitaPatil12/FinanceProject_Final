from django.contrib import admin
from .models import *

# Register your models here.
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ['full_name','gender','mobile','email','city']
admin.site.register(Enquiry,EnquiryAdmin)
