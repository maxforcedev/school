from django.db import models

class Occurrence(models.Model):
    OCCURRENCE_TYPE_CHOICES = [
        ('advertencia', 'Advertência'),
        ('suspensao', 'Suspensão'),
        ('outro', 'Outro'),
    ]

    student = models.ForeignKey('accounts.StudentProfile', on_delete=models.PROTECT)
    recorded_by = models.ForeignKey('accounts.TeacherProfile', on_delete=models.SET_NULL, null=True, blank=True)
    classroom = models.ForeignKey('academic.Classroom', on_delete=models.PROTECT)
    academic_year = models.ForeignKey('academic.AcademicYear', on_delete=models.PROTECT)
    occurrence_type = models.CharField(max_length=20, choices=OCCURRENCE_TYPE_CHOICES)
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return f"{self.student.user.name} - {self.occurrence_type} - {self.date}"
