# Create your views here.

from django.shortcuts import render
from django.conf import settings
from rest_framework import viewsets

from .models import Document
from .serializers import DocumentSerializer


class DocumentViewSet(viewsets.ModelViewSet):
    """
    API Viewset for Documents.
    """
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
