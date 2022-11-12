from django import forms
from django.contrib.auth.models import User

from .models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"


class UserForm(forms.ModelForm):
    confirmpassword = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'confirmpassword')
