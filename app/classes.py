from django.template.defaultfilters import filesizeformat
from django.conf import settings
import magic

#@deconstructible
class FileValidator(object):
	error_messages = {
     	'max_size': ("Ensure this file size is not greater than %d bytes. Your file size is %d bytes."),
     	'min_size': ("Ensure this file size is not less than %(min_size)s. Your file size is %(size)s."),
     	'content_type': "Files of type %ss are not supported.",
    }
	def __init__(self):
		self.max_size = settings.IMAGE_MAX_SIZE
		self.content_types = settings.IMAGE_FORMATS_ALLOWED

	def __call__(self, file):
		#
		#if self.min_size is not None and file.size < self.min_size:
		status = {};
		status['status'] = False
		status['errors'] = []

		if self.max_size is not None and file.size > self.max_size:
			status['errors'].append(self.error_messages['max_size']%(int(self.max_size), int(file.size)))

		if self.content_types:
			content_type = magic.from_buffer(file.read(), mime=True)
			if content_type not in self.content_types:
				status['errors'].append(self.error_messages['content_type']%(str(content_type)))
			else: 
				status['status'] = True
				try:
				    del status['errors']
				except KeyError:
				    pass

		return status