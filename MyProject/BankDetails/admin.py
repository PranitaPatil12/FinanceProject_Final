from django.contrib import admin
from .models import *

# Register your models here.
class BankDetailsAdmin(admin.ModelAdmin):
    list_display = ['account_holder_name','account_no','bank_name','branch_name','account_type','ifsc_code','micr_code']
admin.site.register(BankDetails,BankDetailsAdmin)
