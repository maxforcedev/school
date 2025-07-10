import re
from django.contrib.auth import authenticate, login, get_user_model
from django.views.generic import FormView, View
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib import messages
from django.core.exceptions import ValidationError
from accounts.services  import register_responsible_with_students
from . import forms

class LoginView(FormView):
    template_name = 'accounts/login.html'
    form_class = forms.LoginForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        user = authenticate(self.request, username=username, password=password)

        if user:
            login(self.request, user)
            return redirect(self.get_success_url())
        else:
            form.add_error(None, 'Usuario ou senha não encontradas ou incorretas.')
            return self.form_invalid(form)

    def get_success_url(self):
        user = self.request.user

        if hasattr(user, 'profile'):
            role = user.profile.role
            
            if role == 'responsible':
                return reverse_lazy('responsible_dashboard')
            elif role == 'student':
                return reverse_lazy('student_dashboard')
            elif role == 'teacher':
                return reverse_lazy('teacher_dashboard')
            elif role == 'secretary':
                return reverse_lazy('secretary_dashboard')
            elif role == 'admin':
                return reverse_lazy('admin_dashboard')

        return self.success_url


User = get_user_model()
class RegisterView(View):
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('login')

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        try:
            register_responsible_with_students(request.POST)
        except ValidationError as e:
            messages.error(request, str(e))
            return redirect('register')
        return redirect(self.success_url)