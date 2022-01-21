from django.db import models
from django.contrib.auth.models import AbstractUser

STATUS = (("RELATIONSHIP MANAGER", 'Relationship Manager'), ('OPERATION HEAD', 'Operation Head'), ('OTHER', 'Other'))


class CustomUser(AbstractUser):

    status = models.CharField(max_length=20, choices=STATUS, default='OTHER')
