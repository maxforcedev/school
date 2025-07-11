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
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    role = models.CharField(max_length=15, choices=ROLE_CHOICES)
    addrees = models.TextField(max_length=200, null=True, blank=True)

    def get_role_display(self):
        return dict(self.ROLE_CHOICES).get(self.role, self.role)

    def __str__(self):
        return f'{self.user.name} ({self.role})'
