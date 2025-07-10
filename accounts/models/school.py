from django.db import models
from django.core.validators import RegexValidator


class School(models.Model):

    name = models.CharField(max_length=200)
    cnpj = models.CharField(max_length=14, blank=True, null=True, unique=True, validators=[RegexValidator(regex=r'^\d{14}$', message='CNPJ deve conter 14 dígitos numéricos')])
    address = models.TextField(max_length=300, blank=True, null=True)
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
