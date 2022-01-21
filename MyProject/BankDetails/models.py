from django.db import models
from Customer.models import Customer


# Create your models here.
class BankDetails(models.Model):
    account_type = (
        ('SAVING', 'Saving'),
        ('CURRENT', 'Current'),
        ('SALARIED', 'Salaried')
    )
    customer = models.OneToOneField(Customer,on_delete=models.CASCADE)
    account_holder_name = models.CharField(max_length=100)
    account_no = models.IntegerField()
    bank_name = models.CharField(max_length=100)
    branch_name = models.CharField(max_length=100)
    account_type = models.CharField(max_length=40, choices=account_type)
    ifsc_code = models.CharField(max_length=50)
    micr_code = models.CharField(max_length=100)
