#logs.forms.py

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django import forms

class LoginForm(AuthenticationForm):
	username = forms.CharField(label='Username', max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
	password = forms.CharField(label='Password', max_length=30, widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))

class RegistrationForm(forms.Form):
	username = forms.CharField(label='Username', max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
	password1 = forms.CharField(label='Password', max_length=30, widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password1'}))
	password2 = forms.CharField(label='Re-enter Password', max_length=30, widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password2'}))
	email = forms.CharField(label='Email Address', max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'email'}))
	first_name = forms.CharField(label='First Name', max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'firstname'}))
	last_name = forms.CharField(label='Last Name', max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'lastname'}))

class UploadImageForm(forms.Form):
	title = forms.CharField(label='File Title', max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'file_title'}))
	file = forms.FileField(label='File', widget=forms.ClearableFileInput(attrs={'multiple': True}))
	comment = forms.CharField(label='Comment', max_length=140, widget=forms.Textarea(attrs={'class': 'form-control', 'name': 'file_comment'}))

