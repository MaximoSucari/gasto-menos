from user.models import UserProfile
from django.db import models
from category.models import Category


class Expense(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10)
    message = models.TextField(max_length=255)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True
    )
    date = models.DateField()

    def __str__(self):
        return f"{self.user.phone} - {self.amount} {self.currency} - {self.category}"
