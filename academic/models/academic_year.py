from django.db import models

class AcademicYear(models.Model):
    year = models.CharField(max_length=4, unique=True)
    is_current = models.BooleanField(default=False)

    def __str__(self):
        return self.year
