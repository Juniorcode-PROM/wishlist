from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django import forms


class RegisterForm(forms.Form):
    login = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput,min_length=8)


    def clean_login(self):
        if User.objects.filter(username=self.cleaned_data["login"]).exists():
            raise ValidationError("Пользователь уже был зарегестрирован")
        return self.cleaned_data["login"]

