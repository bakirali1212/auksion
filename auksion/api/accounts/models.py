from django.db import models
from ..base.models import Basemodel
from django.contrib.auth.models import AbstractUser
# Create your models here.
UserRol = (
    ('Client', 'Client'),
    ('Seller', 'Seller'),
)

class Usermodel(Basemodel, AbstractUser):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=10, choices=UserRol)
    phone = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    def __str__(self) -> str:
        return self.name