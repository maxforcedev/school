from django.db import models


class UserDocument(models.Model):
    profile = models.ForeignKey('accounts.Profile', on_delete=models.CASCADE, related_name='documents')

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
