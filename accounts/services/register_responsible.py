import re
from django.contrib.auth import get_user_model
from accounts.models import StudentResponsible
from appconfig.utils import validar_cpf
from django.core.exceptions import ValidationError

User = get_user_model()


def register_responsible_with_students(data):
    required_fields = ['name', 'cpf', 'phone', 'email', 'address', 'number', 'district', 'cep']
    for field in required_fields:
        if not data.get(field, '').strip():
            raise ValidationError(f'The field "{field}" is required.')

    raw_cpf = re.sub(r'\D', '', data['cpf'])
    raw_phone = re.sub(r'\D', '', data['phone'])

    if not validar_cpf(raw_cpf):
        raise ValidationError('Invalid CPF for responsible.')

    if User.objects.filter(email=data['email']).exists():
        raise ValidationError('Email is already in use.')

    if User.objects.filter(cpf=raw_cpf).exists():
        raise ValidationError('CPF is already in use.')

    if User.objects.filter(phone=raw_phone).exists():
        raise ValidationError('Phone is already in use.')

    user = User.objects.create(
        email=data['email'],
        name=data['name'],
        cpf=raw_cpf,
        is_active=False,
        phone=raw_phone
    )
    user.set_password(raw_cpf)
    user.save()

    profile = user.profile
    profile.role = 'responsible'
    profile.address = f"{data.get('address')}, {data.get('number')} - {data.get('district')}, ZIP: {data.get('cep')}"
    profile.save()

    student_indexes = set()

    for key in data.keys():
        if key.startswith("students[") and "][name]" in key:
            idx = key.split('[')[1].split(']')[0]
            student_indexes.add(idx)

    for idx in student_indexes:
        student_name = data.get(f'students[{idx}][name]', '').strip()
        student_cpf = re.sub(r'\D', '', data.get(f'students[{idx}][cpf]', ''))
        student_phone = re.sub(r'\D', '', data.get(f'students[{idx}][phone]', ''))
        student_email = data.get(f'students[{idx}][email]', '').strip()
        relation = data.get(f'students[{idx}][relation]', '').strip()
        birth_date = data.get(f'students[{idx}][birth_date]', '').strip()

        if not (student_name and student_cpf and student_email and student_phone and relation and birth_date):
            raise ValidationError(f'All fields for student {student_name or f"#{idx}"} are required.')

        if not validar_cpf(student_cpf):
            raise ValidationError(f'Invalid CPF for student {student_name}.')

        if User.objects.filter(cpf=student_cpf).exists():
            raise ValidationError(f'CPF for student {student_name} is already in use.')

        if User.objects.filter(email=student_email).exists():
            raise ValidationError(f'Email for student {student_name} is already in use.')

        if User.objects.filter(phone=student_phone).exists():
            raise ValidationError(f'Phone for student {student_name} is already in use.')

        student_user = User.objects.create(
            email=student_email,
            name=student_name,
            cpf=student_cpf,
            is_active=False,
            phone=student_phone
        )
        student_user.set_password(student_cpf)
        student_user.save()

        student_profile = student_user.profile
        student_profile.role = 'student'
        student_profile.save()

        StudentResponsible.objects.create(
            student=student_profile,
            responsible=profile,
            relation=relation
        )
