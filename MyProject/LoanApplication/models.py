from django.db import models
from Customer.models import Customer


class SanctionedLoan(models.Model):
    customer = models.OneToOneField(Customer,on_delete=models.CASCADE)
    required_loan = models.IntegerField(default=None)
    approved_loan = models.IntegerField(null=True)
    tenure = models.IntegerField(null=True)
    interest = models.FloatField(null=True)
    emi = models.FloatField(null=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.customer},{self.required_loan},{self.approved_loan},{self.tenure},{self.interest},{self.emi},{self.is_approved}"
