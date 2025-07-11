from django.views import View
from django.views.generic import ListView
from django.shortcuts import redirect
from django.db.models import Q
from django.contrib import messages
from django.urls import reverse_lazy
from accounts import models
from accounts.services import admin_create_new_user
from django.core.exceptions import ValidationError


class UserListView(ListView):
    model = models.Profile
    template_name = 'accounts/admin/users/list.html'
    context_object_name = 'users'

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        role = self.request.GET.get('role')

        if q:
            queryset = queryset.filter(
                Q(user__name__icontains=q) |
                Q(user__email__icontains=q) |
                Q(user__phone__icontains=q) |
                Q(user__cpf__icontains=q)
            )

        if role:
            queryset = queryset.filter(role=role)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q', '')
        context['selected_role'] = self.request.GET.get('role', '')
        return context


class UserCreateView(View):
    def post(self, request):
        try:
            admin_create_new_user(
                nome=request.POST.get('name'),
                cpf=request.POST.get('cpf'),
                phone=request.POST.get('phone'),
                email=request.POST.get('email'),
                role=request.POST.get('role'),
            )
            messages.success(request, "Usuário criado com sucesso!")
        except ValidationError as e:
            messages.error(request, str(e))
        except Exception:
            messages.error(request, "Erro inesperado ao criar usuário.")
        return redirect(reverse_lazy('adm_list_user'))
