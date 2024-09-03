from django.db import models

# Create your models here.
class std(models.Model):
    Name =models.CharField(max_length=20,blank=False)
    Roll_No = models.IntegerField(max_length=2,blank=False,unique=True)
    Department = models.CharField(max_length=50,blank=False)
    session = models.CharField(max_length=10,blank=False)

    def __str__(self):
        return self.Name