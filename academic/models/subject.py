from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=100)
    teachers = models.ManyToManyField('accounts.TeacherProfile', blank=True)

    def __str__(self):
        return self.name
