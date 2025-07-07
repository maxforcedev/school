from django.db import models
from django.core.validators import RegexValidator
from django.conf import settings

phone_validator = RegexValidator(
    regex=r'^\d{11}$',
    message='O número de telefone deve conter 11 dígitos. (00) 00000-0000'
)


class SecretaryProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=14)
    phone = models.CharField(max_length=11, validators=[phone_validator], blank=True, null=True)
    photo = models.ImageField(upload_to='staff/photos/', blank=True, null=True)

    def __str__(self):
        return self.user