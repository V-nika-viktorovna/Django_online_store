from django import forms
from django.contrib.auth.forms import UserCreationForm

from catalog.forms import ProductStyleMixin
from users.models import User


class UserCreateForm(ProductStyleMixin, UserCreationForm):
    username = forms.CharField(max_length=30)

    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2')
