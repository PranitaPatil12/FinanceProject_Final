from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

gender_choice = (('Male','Male'),('Female','Female'),('Other','Other'))

class LoanDetails(models.Model):
    full_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=32,choices=gender_choice)
    dob = models.DateField()
    mobile = PhoneNumberField(unique=True)
    email = models.EmailField(unique=True)
    pan_number = models.CharField(max_length=32)
    required_loan = models.IntegerField()
    cibil_score = models.IntegerField(default=None)
    is_eligible = models.BooleanField(default=False)


    def __str__(self):
        return self.full_name

class Enquiry(models.Model):
    full_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=30,choices=gender_choice)
    mobile = PhoneNumberField()
    email = models.EmailField(unique=True)
    city = models.CharField(max_length=30)

    def _str_(self):
        return f"{self.full_name},{self.gender},{self.mobile},{self.email},{self.city}"