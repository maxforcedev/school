from django.db import models


class Tuition(models.Model):
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('pago', 'Pago'),
        ('atrasado', 'Atrasado'),
    ]

    student = models.ForeignKey('accounts.Profile', on_delete=models.PROTECT, limit_choices_to={'role': 'student'})
    responsible = models.ForeignKey('accounts.Profile', on_delete=models.PROTECT, limit_choices_to={'role': 'teacher'})
    academic_year = models.ForeignKey('academic.AcademicYear', on_delete=models.PROTECT)
    due_date = models.DateField()
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pendente')
    reference_month = models.CharField(max_length=7)
    payment_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.student.user.name} - {self.reference_month} - {self.status}"
