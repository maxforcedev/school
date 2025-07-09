from django.views.generic import FormView
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.urls import reverse_lazy
from .forms import LoginForm


class LoginView(FormView):
    template_name = 'accounts/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(self.request, username=username, password=password)
        
        if user:
            login(self.request, user)
            return redirect(self.get_success_url())
        else:
            form.add_error(None, 'Credenciais inválidas')
            return self.form_invalid(form)