from django.views.generic import View
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib import messages
from django.core.exceptions import ValidationError
from accounts.services import register_responsible_with_students


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
