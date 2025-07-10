from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label="CPF, Telefone ou E-mail")
    password = forms.CharField(widget=forms.PasswordInput)
