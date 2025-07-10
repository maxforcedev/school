from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
import re

User = get_user_model()

class CPFPhoneEmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        if not username or not password:
            return None

        username_clean = re.sub(r'\D', '', username)

        user = User.objects.filter(email__iexact=username).first()

        if not user:
            user = User.objects.filter(cpf=username_clean).first()

        if not user:
            user = User.objects.filter(phone=username_clean).first()

        if user and user.check_password(password):
            return user

        return None
