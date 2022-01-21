from django.db import models
from Customer.models import Customer
# Create your models here.
class Documents(models.Model):
    customer = models.OneToOneField(Customer,on_delete=models.CASCADE)
    pan_card = models.FileField(upload_to='files', default='')
    aadhar_card = models.FileField(upload_to='files', default='')
    bank_statment = models.FileField(upload_to='files', default='')
    photo = models.ImageField(upload_to='image', default='')
    signature = models.ImageField(upload_to='image', default='')
    salary_slip = models.FileField(upload_to='files', default='')
    from16 = models.FileField(upload_to='files', default='')
    blance_sheet = models.FileField(upload_to='files', default='')
    itr = models.FileField(upload_to='files', default='')
    business_proof = models.FileField(upload_to='files', default='')

    def __str__(self):
        return f'{self.pan_card}'