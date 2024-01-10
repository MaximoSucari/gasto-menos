# yourapp/models.py
from django.db import models


class UserProfile(models.Model):
    phone = models.CharField(max_length=50)

    def __str__(self):
        return self.phone
