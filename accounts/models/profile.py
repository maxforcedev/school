from django.db import models
from django.conf import settings

class Profile(models.Model):
    ROLE_CHOICES = [
        ('admin', 'Administração Geral'),
        ('secretary', 'Secretaria'),
        ('diretion', 'Direção'),
        ('coordinator', 'Coordenação Pedagógica'),
        ('teacher', 'Professor(a)'),
        ('student', 'Aluno(a)'),
        ('responsible', 'Responsável'),
        ('support', 'Apoio Escolar'),
    ]

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, unique=True)
    cpf = models.CharField(max_length=14, unique=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    role = models.CharField(max_length=15, choices=ROLE_CHOICES)

    def __str__(self):
        return f'{self.user.name} ({self.role})'

