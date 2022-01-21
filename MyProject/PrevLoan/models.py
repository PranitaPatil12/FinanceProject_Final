from django.db import models
from Customer.models import Customer

CHOICES = (
    ('PERSONAL', 'Personal'),
    ('VEHICLE', 'Vehicle'),
    ('HOME', 'Home')
)


class PrevLoan(models.Model):
    customer=models.ForeignKey (Customer,on_delete=models.CASCADE,null= True)
    bank_name = models.CharField(max_length=50,null= True)
    branch_name = models.CharField(max_length=50,null= True)
    account_no = models.IntegerField(null= True)
    ifsc_code = models.CharField(max_length=11,null= True)
    micr_code = models.CharField(max_length=9,null= True)
    loan_amount = models.FloatField(null= True)
    loan_type = models.CharField(max_length=10, choices=CHOICES,null= True)
    loan_tenure = models.FloatField(null= True)
    amount_paid = models.FloatField(null= True)

