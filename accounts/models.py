# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    SERVICE_CHOICES = [
        ('financial', 'Financial Planning'),
        ('healthcare', 'Healthcare Solutions'),
        ('insurance', 'Insurance Coverage'),
        ('investment', 'Investment Management'),
        ('comprehensive', 'Comprehensive Package'),
    ]

    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    service_interest = models.CharField(
        max_length=20,
        choices=SERVICE_CHOICES,
        default='financial'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return self.email

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}".strip()