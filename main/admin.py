from django.contrib import admin
from .models import expenses, Transactions
 
# Register your models here.

admin.site.register(expenses)
admin.site.register(Transactions)