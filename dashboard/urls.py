from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/aluno/', views.dashboard_aluno, name='student_dashboard'),
]
