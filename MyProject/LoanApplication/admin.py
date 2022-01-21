from django.contrib import admin
from .models import *

# Register your models here.
class SanctionedLoanAdmin(admin.ModelAdmin):
    list_display = ['customer','required_loan','approved_loan','interest','tenure', 'emi','is_approved']
admin.site.register(SanctionedLoan,SanctionedLoanAdmin)