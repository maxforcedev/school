from  django.db import models
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


class UserDocument(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='documents')

    DOCUMENT_TYPE_CHOICES = [
        ('rg', 'RG'),
        ('cpf', 'CPF'),
        ('certidao', 'Certidão de Nascimento'),
        ('historico', 'Histórico Escolar'),
        ('comprovante', 'Comprovante de Residência'),
        ('contrato', 'Contrato'),
        ('outro', 'Outro'),
    ]

    document_type = models.CharField(max_length=30, choices=DOCUMENT_TYPE_CHOICES)
    file = models.FileField(upload_to='documents/')
    description = models.TextField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.get_document_type_display()} - {self.profile.user.name}'
