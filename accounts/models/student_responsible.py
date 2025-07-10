from django.db import models
from django.core.exceptions import ValidationError


class StudentResponsible(models.Model):
    RELATION_CHOICES = [
        ('father', 'Pai'),
        ('mother', 'Mãe'),
        ('stepfather', 'Padrasto'),
        ('stepmother', 'Madrasta'),
        ('grandparent', 'Avô/Avó'),
        ('legal_guardian', 'Tutor Legal'),
        ('other', 'Outro'),
    ]

    student = models.ForeignKey(
        'accounts.Profile',
        on_delete=models.PROTECT,
        related_name='responsibles_links', 
        limit_choices_to={'role': 'student'}
        
    )
    responsible = models.ForeignKey(
        'accounts.Profile',
        on_delete=models.PROTECT,
        related_name='students_links',
        limit_choices_to={'role': 'responsible'}
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
