from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.db import models
from django.conf import settings
from django.utils import timezone

from app.forms import *
from app.classes import * 
from app.models import *

import hashlib
import os
import datetime

@login_required(login_url="login", redirect_field_name=None)

def home(request):
	images = []
	for file in Image.objects.all():
		image = {}
		image['filename'] = file.filename
		image['url'] = '/' + settings.IMAGE_BASE_URL + file.filename_hash
		images.append(image)
	return render(request, "home.html", {'images': images})

@csrf_protect
def register(request):
	if request.method == 'GET':
		return render(request, "register.html", {'form': RegistrationForm()})

	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			user = User.objects.create_user(
				username=form.cleaned_data['username'],
				password=form.cleaned_data['password1'],
				email=form.cleaned_data['email'],
				first_name=form.cleaned_data['first_name'],
				last_name=form.cleaned_data['last_name'],
			)
			request.session['reg_success'] = True
			return HttpResponseRedirect('/registersuccess')
	
def register_success(request):
	if ('reg_success' in request.session) and request.session['reg_success']:
		del request.session['reg_success']
		return render(request, 'success.html')
	else:
		return HttpResponseRedirect('/')

def upload_file(request):
	if request.user.is_authenticated:
		if request.method == 'GET':
			return render(request, 'upload.html', {'form': UploadImageForm()})

		if request.method == 'POST':
			form = UploadImageForm(request.POST, request.FILES)
			if form.is_valid():
				#handle_uploaded_file(request.FILES['file'])
				validate_file = FileValidator()
				status = validate_file(request.FILES['file']) 

				if status['status']:
					
					#validate filename here
					filename = str(datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')) + str(request.FILES['file'].name)
					filename_hash = hashlib.sha256(filename).hexdigest()
					file_location = settings.IMAGE_BASE_URL + str(filename_hash)
					
					try:
						image = Image(filename=filename, filename_hash=filename_hash, file_comment=form.cleaned_data['comment'], uploaded_at=timezone.now(), owner=request.user)
						image.save()
						handle_uploaded_file(request.FILES['file'], file_location)

					except Exception, e:
						# Add exception handling code here
						status['status'] = False
						status['error'] = e
						return render(request, 'upload.html', {'form': UploadImageForm(), 'status': status})

				return render(request, 'upload.html', {'form': UploadImageForm(), 'status': status})
			else:
				return render(request, 'upload.html', {'form': UploadImageForm()})
		return HttpResponseRedirect('/')
	else:
		return HttpResponseRedirect('/')

def upload_success(request):
	if request.user.is_authenticated:
		if request.method == 'GET':
			return render(request, 'upload_success.html')

def handle_uploaded_file(file, file_location):
	with open(file_location, 'wb+') as destination:
		for chunk in file.chunks():
			destination.write(chunk)

