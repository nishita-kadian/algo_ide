from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
# from django.contrib.auth.models import User
from .models import *


class UserForm(ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('email','username','password')
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


# class CreateUserForm():
#     password = forms.CharField(widget=forms.PasswordInput)
#     # name = forms.CharField()
#     # username = forms.Textarea(widgets=forms.TextInput)

#     class Meta:
#         model = User
#         # widgets = {
#         #     'password': forms.PasswordInput(),
#         # }
#         fields = ['username', 'name', 'email', 'password1', 'password2']
