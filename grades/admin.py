from django.contrib import admin
from .models import Grade


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ('student', 'subject', 'classroom', 'academic_year', 'grade', 'date_recorded')
    list_filter = ('academic_year', 'classroom', 'subject')
    search_fields = ('student__user__name', 'student__user__email', 'subject__name', 'classroom__name')
    ordering = ('-date_recorded',)