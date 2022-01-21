from django.contrib import admin
from .models import Customer

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['full_name','guardian_name','gender','mobile','email','pan_no','aadhar_card','marital_status','religion','dob']
admin.site.register(Customer,CustomerAdmin)