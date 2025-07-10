from django.db import models


class Classroom(models.Model):  # Turma
    name = models.CharField(max_length=100)
    year = models.CharField(max_length=4)
    shift = models.CharField(max_length=20, choices=[('manhã', 'Manhã'), ('tarde', 'Tarde'), ('noite', 'Noite')])
    academic_year = models.ForeignKey('academic.AcademicYear', on_delete=models.PROTECT)
    school = models.ForeignKey('accounts.School', on_delete=models.PROTECT)
    subjects = models.ManyToManyField('academic.Subject', related_name='classrooms', blank=True)

    def __str__(self):
        return f"{self.name} ({self.year}) - {self.school.name}"
