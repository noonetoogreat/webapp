from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Image(models.Model):
	#document = models.FileField(upload_to='documents/')
	uploaded_at = models.DateTimeField(auto_now_add=True)
	filename = models.CharField(max_length=512, blank=True)
	filename_hash = models.CharField(max_length=512, blank=True)
	file_comment = models.CharField(max_length=512, blank=True)
	owner = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.filename

