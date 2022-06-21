from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import *


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Myuser
        fields = '__all__'


class MyUserCreationForm(UserCreationForm):

    class Meta:
        model = Myuser
        fields = ('phone',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = Myuser
        fields = ('phone',)