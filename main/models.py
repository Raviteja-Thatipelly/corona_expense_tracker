from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Transactions(models.Model):
    transactions_type = [
        ("income", "INCOME"),
        ("expenses", "EXPENSES")
    ]
    
    type = models.CharField(max_length=10, choices=transactions_type, default='Income')
    source = models.CharField(max_length=100, null=True, blank=True)
    paid_to = models.CharField(max_length=100, null=True, blank=True)
    category = models.CharField(max_length=50, null=True, blank=True)
    mode_of_payment = models.CharField(max_length=20, default='cash')
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    currency = models.CharField(max_length=10, default='INR')
    description = models.TextField(blank=True, null=True)
    date = models.DateTimeField()
    invoice = models.FileField(upload_to='invoices/', blank=True, null=True)

    
    def __str__(self):
        return f" {self.type} - {self.amount}"    
    
    
class Loan(models.Model):
    loan_status = [
        ("Ongoing", "ongoing"),
        ("Completed", "completed")
    ]
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=loan_status)
    created_at = models.DateField(auto_now_add=True)
            
    def __str__(self):
        return f"{self.name}-{self.status}"