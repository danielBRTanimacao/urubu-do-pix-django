from django.db import models
from django.contrib.auth.models import AbstractUser
from decimal import Decimal

class User(AbstractUser):
    amount = models.DecimalField(max_digits=15, decimal_places=2, default=Decimal('0.00'))
