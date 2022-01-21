from django.contrib import admin
from .models import Guarantor




class guarantorAdmin(admin.ModelAdmin):
    list_display = ['guarantor_name', 'relation_with_cust', 'profession', 'contact_no',
                    'aadhar_no', 'pan_no', 'house_no', 'landmark', 'area', 'city', 'pincode', 'state', 'country']


admin.site.register(Guarantor, guarantorAdmin)
