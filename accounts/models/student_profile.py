from  django.db import models
from django.core.validators import RegexValidator
from django.conf import settings

phone_validator = RegexValidator(
    regex=r'^\d{11}$',
    message='O número de telefone deve conter 11 dígitos. (00) 00000-0000'
)


class StudentDocument(models.Model):
    student = models.ForeignKey('StudentProfile', on_delete=models.CASCADE, related_name='documents')
    file = models.FileField(upload_to='students/documents/')
    name = models.CharField(max_length=100)  # ex: "RG", "CPF", "Histórico Escolar"
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_relation_display()} de {self.student.user}"


class StudentProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=14)
    phone = models.CharField(max_length=11, validators=[phone_validator], blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='students/photos/', blank=True, null=True)

    def __str__(self):
        return self.user