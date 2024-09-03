from django.db import models

# Create your models here.
class std(models.Model):
    Name =models.CharField(max_length=20)
    Roll_No = models.IntegerField(max_length=2)
    Department = models.CharField(max_length=50)
    session = models.CharField(max_length=10)