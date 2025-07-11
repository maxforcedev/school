import re
from django.contrib.auth.models import User
from accounts.models import Profile
from django.core.exceptions import ValidationError
from appconfig.utils import validar_cpf


def admin_create_new_user(nome, cpf, phone, email, role):
    if not all([nome, cpf, phone, email, role]):
        raise ValidationError("Todos os campos são obrigatórios.")

    raw_cpf = re.sub(r'\D', '', cpf)
    raw_phone = re.sub(r'\D', '', phone)

    if not validar_cpf(raw_cpf):
        raise ValidationError('O CPF informado é invalido.')

    if User.objects.filter(email=email).exists():
        raise ValidationError("Já existe um usuário com este e-mail cadastrado.")
    elif User.objects.filter(phone=raw_phone).exists():
        raise ValidationError("Já existe um usuário com este telefone cadastrado.")
    elif User.objects.filter(cpf=raw_cpf).exists():
        raise ValidationError("Já existe um usuário com este cpf cadastrado.")

    user = User.objects.create_user(
        username=email,
        email=email,
        password=raw_cpf
    )

    Profile.objects.create(
        user=user,
        name=nome,
        cpf=raw_cpf,
        phone=raw_phone,
        role=role
    )

    return user
