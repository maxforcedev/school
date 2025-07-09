from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=100)
    teachers = models.ManyToManyField('accounts.Profile', blank=True, limit_choices_to={'role': 'teacher'})

    def __str__(self):
        return self.name
