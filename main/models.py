from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Transactions(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name
    
class expenses(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE),
    Transactions = models.ForeignKey(Transactions, on_delete=models.SET_NULL, null=True, blank=True),
    amount = models.DecimalField(max_digits=10, decimal_places=2),
    description = models.TextField(blank=True, null=True),
    date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.amount} ({self.category})"    