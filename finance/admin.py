from django.contrib import admin
from .models import Tuition

@admin.register(Tuition)
class TuitionAdmin(admin.ModelAdmin):
    list_display = ('student', 'responsible', 'reference_month', 'due_date', 'amount', 'status', 'payment_date')
    list_filter = ('status', 'academic_year', 'reference_month')
    search_fields = ('student__user__name', 'responsible__user__name')
    date_hierarchy = 'due_date'
