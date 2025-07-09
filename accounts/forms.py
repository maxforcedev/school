from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label='Email, Celular ou CPF')
    passworld = forms.CharField(widget=forms.PasswordInput)


"""class CreateUserForm(forms.Form):
    """