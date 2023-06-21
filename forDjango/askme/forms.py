from django import forms
from app import models
from django.contrib import auth
from django.utils.translation import gettext_lazy as _
from django.http import HttpRequest


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput(), max_length=80, min_length=6)