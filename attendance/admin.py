from django.contrib import admin
from .models import Attendance


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'classroom', 'date', 'was_present', 'academic_year', 'recorded_by')
    list_filter = ('academic_year', 'classroom', 'was_present')
    search_fields = ('student__user__name', 'classroom__name', 'recorded_by__user__name')
    date_hierarchy = 'date'
