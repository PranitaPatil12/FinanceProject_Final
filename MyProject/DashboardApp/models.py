from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

GENDER=(
    ("Male","Male"),
    ("Female","Female"),
    ("Other","Other"),
)
STATUS=(
    ("Married","Married"),
    ("Unmarried","Unmarried"),
)
RELIGION=(
    ("Hinduism","Hinduism"),
    ("Islam","Islam"),
    ("Christianity","Christianity"),
    ("Sikhism","Sikhism"),
    ("Other","Other"),
)

class Customer(models.Model):
    full_name = models.CharField(max_length=60)
    guardian_name = models.CharField(max_length=60)
    gender = models.CharField(max_length=60,choices=GENDER)
    mobile = PhoneNumberField(null=False,blank=False)
    email = models.EmailField()
    pan_no = models.CharField(max_length=30)
    aadhar_card = models.IntegerField()
    marital_status = models.CharField(max_length=60,choices=STATUS)
    religion = models.CharField(max_length=60,choices=RELIGION)
    dob = models.DateTimeField()



