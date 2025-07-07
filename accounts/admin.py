from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


class CustomUserAdmin(UserAdmin):
    model = models.CustomUser
    list_display = ('email', 'name', 'is_active', 'is_staff', 'is_superuser')
    search_fields = ('email', 'name')
    ordering = ('email',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Informações pessoais', {'fields': ('name',)}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Datas importantes', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'password1', 'password2', 'is_staff', 'is_superuser'),
        }),
    )


class StudentDocumentInline(admin.TabularInline):
    model = models.StudentDocument
    extra = 1


@admin.register(models.StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'cpf', 'phone')
    search_fields = ('user__email', 'cpf')
    inlines = [StudentDocumentInline]


@admin.register(models.TeacherProfile)
class TeacherProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ('user__email', 'user__name')


@admin.register(models.ResponsibleProfile)
class ResponsibleProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ('user__email', 'user__name')


@admin.register(models.SecretaryProfile)
class SecretaryProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ('user__email', 'user__name')


@admin.register(models.School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name', 'cnpj')
    search_fields = ('name', 'cnpj')


@admin.register(models.StudentResponsible)
class StudentResponsibleAdmin(admin.ModelAdmin):
    list_display = ('student', 'responsible', 'relation')
    search_fields = ('student__user__email', 'responsible__user__email', 'relation')


admin.site.register(models.CustomUser, CustomUserAdmin)
