from django.db import models
from accounts.models import Profile
from django.core.exceptions import ValidationError


class StudentResponsible(models.Model):
    RELATION_CHOICES = [
        ('father', 'Pai'),
        ('mother', 'Mãe'),
        ('stepfather', 'Padrasto'),
        ('stepmother', 'Madrasta'),
        ('grandparent', 'Avô/Avó'),
        ('sibling', 'Irmão/Irmã'),
        ('uncle_aunt', 'Tio/Tia'),
        ('legal_guardian', 'Tutor Legal'),
        ('other', 'Outro'),
    ]

    student = models.ForeignKey(
        Profile,
        on_delete=models.PROTECT,
        related_name='responsibles_links'
    )
    responsible = models.ForeignKey(
        Profile,
        on_delete=models.PROTECT,
        related_name='students_links'
    )
    relation = models.CharField(max_length=20, choices=RELATION_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if self.student.role != 'student':
            raise ValidationError('O perfil vinculado como aluno não tem o papel de aluno.')
        if self.responsible.role != 'responsible':
            raise ValidationError('O perfil vinculado como responsável não tem o papel de responsável.')

    def __str__(self):
        return f"{self.relation or 'Responsável'} de {self.student.user.name}"
