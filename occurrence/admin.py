from django.contrib import admin
from .models import Occurrence

@admin.register(Occurrence)
class OccurrenceAdmin(admin.ModelAdmin):
    list_display = ('student', 'occurrence_type', 'classroom', 'date', 'academic_year', 'recorded_by')
    list_filter = ('occurrence_type', 'academic_year', 'classroom')
    search_fields = ('student__user__name', 'description', 'recorded_by__user__name')
    date_hierarchy = 'date'
