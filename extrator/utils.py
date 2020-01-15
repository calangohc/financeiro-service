#!/usr/bin/env python3.7
import os
from uuid import uuid4

from django.conf import settings
from django.utils.deconstruct import deconstructible


@deconstructible
class PathRename(object):

    def __init__(self, sub_path):
        self.sub_path = sub_path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]

        if instance.pk:
            filename = f'{instance.pk}.{ext}'
        else:
            filename = f'{uuid4().hex}.{ext}'

        return os.path.join(self.sub_path, filename)


path_rename = PathRename('docs/')
