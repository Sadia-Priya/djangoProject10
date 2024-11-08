from django.db import models

# Create your models here.
class BankAccount(models.Model):
    owner=models.CharField(max_length=20)
    phone=models.CharField(max_length=30)
    balance=models.FloatField(default=500)
    address=models.CharField(max_length=50)

    def __str__(self):
        return self.owner
