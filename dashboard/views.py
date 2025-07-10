from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def dashboard_aluno(request):
    return render(request, 'dashboard/student_dashboard.html')