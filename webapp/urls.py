"""webapp URL Configuration
"""
from django.conf.urls import url, include
from django.contrib import admin

from django.contrib.auth import views
from app.forms import LoginForm

urlpatterns = [
	url(r'', include('app.urls')),
    url(r'^login/$', views.login, { 'template_name': 'login.html', 'authentication_form': LoginForm, 'redirect_authenticated_user': True}, name='login'),
	url(r'^logout/$', views.logout, {'next_page': '/login'}),
]
