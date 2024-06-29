# forms.py
from django import forms
from .models import User
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'phone_number', 'gender','agree_to_terms']
        widgets = {
            'password': forms.PasswordInput(),
        }