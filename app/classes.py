from django.template.defaultfilters import filesizeformat
from django.conf import settings
import magic

#@deconstructible
class FileValidator(object):
	def __init__(self):
		self.max_size = settings.IMAGE_MAX_SIZE
		self.content_types = settings.IMAGE_FORMATS_ALLOWED

	def __call__(self, file):
		#if self.max_size is not None and file.size > self.max_size:
		#if self.min_size is not None and file.size < self.min_size:
		status = {};
		status['status'] = False

		if self.content_types:
			content_type = magic.from_buffer(file.read(), mime=True)
			if content_type not in self.content_types:
				status['error'] = "invlaid file type"
			else: 
				status['status'] = True

		return status