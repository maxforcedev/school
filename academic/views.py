from django.views.generic import ListView
from . import models


class SubjectListView(ListView):
    model = models.Subject
    template_name = 'academic/subject_list.html'
    context_object_name = 'subjects'
