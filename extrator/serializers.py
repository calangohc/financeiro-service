#!/usr/bin/env
from rest_framework import serializers

from .models import Document


class DocumentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Document
        fields = ['description', 'paypal_document', 'mp_document', 'cef_document', 'uploaded_at']
