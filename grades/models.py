from django.db import models


class Grade(models.Model):
    student = models.ForeignKey('accounts.Profile', on_delete=models.PROTECT, limit_choices_to={'role': 'student'})
    subject = models.ForeignKey('academic.Subject', on_delete=models.PROTECT)
    classroom = models.ForeignKey('academic.Classroom', on_delete=models.PROTECT)
    academic_year = models.ForeignKey('academic.AcademicYear', on_delete=models.PROTECT)
    grade = models.DecimalField(max_digits=5, decimal_places=2)
    evaluation_name = models.CharField(max_length=100, blank=True, null=True)
    date_recorded = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.user.name} - {self.subject.name} - {self.grade}"
