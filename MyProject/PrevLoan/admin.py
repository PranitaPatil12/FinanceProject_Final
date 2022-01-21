from django.contrib import admin
from .models import PrevLoan


class PrevLoanAdmin(admin.ModelAdmin):
    list_display = ['bank_name', 'branch_name', 'account_no', 'ifsc_code', 'micr_code', 'loan_amount', 'loan_type',
                    'loan_tenure', 'amount_paid']


admin.site.register(PrevLoan, PrevLoanAdmin)
