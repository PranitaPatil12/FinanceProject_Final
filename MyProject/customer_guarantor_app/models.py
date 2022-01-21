from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from Customer.models import Customer


class Guarantor(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)

    guarantor_name = models.CharField(max_length=40)
    relation_with_cust = models.CharField(max_length=40)
    profession = models.CharField(max_length=40)
    contact_no = PhoneNumberField(unique=True)
    aadhar_no = models.CharField(max_length=12)
    pan_no = models.CharField(max_length=10)
    house_no = models.CharField(max_length=10)
    landmark = models.CharField(max_length=400)
    area = models.CharField(max_length=40)
    city = models.CharField(max_length=40)
    pincode = models.IntegerField()
    state = models.CharField(max_length=20)
    country = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.guarantor_name}'
