from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/academic/subject', views.SubjectListView.as_view(), name='subject_list')
]
