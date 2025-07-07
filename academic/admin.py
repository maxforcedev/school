from django.contrib import admin
from .models import Classroom, Subject, Enrollment


@admin.register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'shift', 'school')
    list_filter = ('school', 'year', 'shift')
    search_fields = ('name', 'school__name')


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    filter_horizontal = ('teachers',)  # interface mais amigável no admin


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'classroom', 'date_enrolled', 'is_active')
    list_filter = ('is_active', 'classroom')
    search_fields = ('student__user__name', 'student__user__email', 'classroom__name')
