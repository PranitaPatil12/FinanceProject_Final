from django.contrib import admin
from .models import ProfessionalDetails


# Register your models here.

class ProfessionalDetailsModelAdmin(admin.ModelAdmin):
    list_display = ['type_employment', 'designation', 'year_of_exp', 'joining_date', 'monthly_income', 'mode_of_salary', 'company_address','business_name', 'itr', 'avg_monthly_income', 'annual_turnover']


admin.site.register(ProfessionalDetails, ProfessionalDetailsModelAdmin)

