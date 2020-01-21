from django.shortcuts import render
from rest_framework import viewsets

from .models import Ledger
from .serializers import LedgerSerializer


class LedgerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Ledger.objects.all()
    serializer_class = LedgerSerializer
