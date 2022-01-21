from django.db import models
from Customer.models import Customer


# Create your models here.



class ProfessionalDetails(models.Model):
    SALARY_MODE = (

        ('ONLINE', 'Online'),
        ('CHEQUE', 'Cheque'),
        ('CASH', 'Cash'),
    )


    EMPLOYEMENT_TYPE = (

        ('SALARIED', 'Salaried'),
        ('SELF-SALARIED', 'Self-Salaried'),
    )

    IT_RETURNS = (

        ('YES', 'Yes'),
        ('NO', 'No'),
    )
    customer = models.OneToOneField(Customer,on_delete=models.CASCADE)
    type_employment = models.CharField(max_length=50, choices=EMPLOYEMENT_TYPE , null=True)
    designation = models.CharField(max_length=32,blank=True)
    year_of_exp = models.FloatField(null=True)
    joining_date = models.DateField(null=True)
    monthly_income = models.FloatField(null=True)
    mode_of_salary = models.CharField(max_length=50, choices=SALARY_MODE, null=True, default='ONLINE')
    company_address = models.CharField(max_length=100,null=True)

    business_name = models.CharField(max_length=100,null=True)
    itr = models.CharField(max_length=50, choices=IT_RETURNS,null=True, default='YES')
    avg_monthly_income = models.FloatField(null=True)
    annual_turnover = models.FloatField(null=True)


    def __str__(self):
        return f"{self.company_address},{self.designation},{self.year_of_exp},{self.joining_date},{self.monthly_income},{self.mode_of_salary},{self.business_name},{self.itr},{self.avg_monthly_income},{self.annual_turnover}"



