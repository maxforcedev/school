from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models
from django.utils.translation import gettext_lazy as _


class CustomUserAdmin(UserAdmin):
    model = models.CustomUser
    list_display = ('email', 'name', 'cpf', 'phone', 'is_active', 'is_staff', 'is_superuser')
    search_fields = ('email', 'name', 'cpf', 'phone')
    ordering = ('email',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Informações pessoais'), {'fields': ('name', 'cpf', 'phone')}),
        (_('Permissões'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Datas importantes'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'cpf', 'phone', 'password1', 'password2', 'is_staff', 'is_superuser'),
        }),
    )


class UserDocumentInline(admin.TabularInline):
    model = models.UserDocument
    extra = 1


@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'cpf', 'phone')
    search_fields = ('user__email', 'user__name', 'cpf', 'phone')
    list_filter = ('role',)
    inlines = [UserDocumentInline]


@admin.register(models.School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name', 'cnpj')
    search_fields = ('name', 'cnpj')


@admin.register(models.StudentResponsible)
class StudentResponsibleAdmin(admin.ModelAdmin):
    list_display = ('student', 'responsible', 'relation', 'created_at')
    search_fields = (
        'student__user__email',
        'responsible__user__email',
        'relation',
    )
    list_filter = ('relation',)

admin.site.register(models.CustomUser, CustomUserAdmin)
