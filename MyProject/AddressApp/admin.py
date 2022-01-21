from django.contrib import admin
from .models import PermanentAddress,CurrentAddress

# Register your models here.

class PermanentAddressAdmin(admin.ModelAdmin):
    list_display = ['id','flat_no','street_name','city','pincode','area','landmark','district','state','country']
admin.site.register(PermanentAddress,PermanentAddressAdmin)

class CurrentAddressAdmin(admin.ModelAdmin):
    list_display = ['id','flat_no_1','street_name_1','city_1','pincode_1','area_1','landmark_1','district_1','state_1','country_1']
admin.site.register(CurrentAddress,CurrentAddressAdmin)