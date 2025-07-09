from django.db import models
from django.db import models


class Attendance(models.Model):
    student = models.ForeignKey('accounts.StudentProfile', on_delete=models.PROTECT)
    classroom = models.ForeignKey('academic.Classroom', on_delete=models.PROTECT)
    academic_year = models.ForeignKey('academic.AcademicYear', on_delete=models.PROTECT)
    date = models.DateField()
    was_present = models.BooleanField(default=True)
    recorded_by = models.ForeignKey('accounts.TeacherProfile', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        status = "Presente" if self.was_present else "Faltou"
        return f"{self.student.user.name} - {self.date} - {status}"
