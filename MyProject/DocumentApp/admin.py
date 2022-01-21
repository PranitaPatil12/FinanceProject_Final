from django.contrib import admin
from .models import Documents

class DocumentsAdmin(admin.ModelAdmin):
    list_display = ['pan_card','aadhar_card','bank_statment','photo','signature','salary_slip','from16','blance_sheet','itr','business_proof']
admin.site.register(Documents,DocumentsAdmin)
# Register your models here.
