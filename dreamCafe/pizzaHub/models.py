from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PizzaInfo(models.Model):
  pizzaName = models.CharField(max_length=20)
  description = models.CharField(max_length=500)
  image = models.ImageField()
  price = models.FloatField(default=0.00)