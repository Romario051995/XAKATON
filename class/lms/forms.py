from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label="Password", widget=forms.PasswordInput)


class SolutionForm(forms.Form):
    solution = forms.CharField(label='Решение')
