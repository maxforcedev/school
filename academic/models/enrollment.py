from django.db import models

class Enrollment(models.Model):
    student = models.ForeignKey('accounts.Profile', on_delete=models.PROTECT, limit_choices_to={'role': 'student'})
    classroom = models.ForeignKey('academic.Classroom', on_delete=models.PROTECT)
    date_enrolled = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    academic_year = models.ForeignKey('academic.AcademicYear', on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.student.user.name} - {self.classroom.name}"
