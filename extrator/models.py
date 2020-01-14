from django.conf import settings
from django.db import models

from .utils import path_rename


class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    paypal_document = models.FileField(upload_to=path_rename)
    mp_document = models.FileField(upload_to=path_rename)
    cef_document = models.FileField(upload_to=path_rename)
    uploaded_at = models.DateTimeField(auto_now_add=True)
