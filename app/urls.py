#app.urls.py

from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^register/$', views.register, name='register'),
	url(r'^registersuccess', views.register_success, name='register_success'),

	url(r'^upload/$', views.upload_file, name='uploadimage'),
	url(r'^uploadsuccess/$', views.upload_success, name='upload_success' )
]