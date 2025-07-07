from  django.db import models


class StudentResponsible(models.Model):
    RELATION_CHOICES = [
        ('pai', 'Pai'),
        ('mae', 'Mãe'),
        ('avo', 'Avô/Avó'),
        ('tutor', 'Tutor Legal'),
        ('outro', 'Outro'),
    ]
    
    student = models.ForeignKey('accounts.StudentProfile', on_delete=models.PROTECT, related_name='responsibles_links')
    responsible = models.ForeignKey('accounts.ResponsibleProfile', on_delete=models.PROTECT, related_name='students_links')
    relation = models.CharField(max_length=20, choices=RELATION_CHOICES)  # Ex: "pai", "mãe", "tutor legal"
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.relation or 'Responsável'} de {self.student.user}"
