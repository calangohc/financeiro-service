#!/usr/bin/env
from rest_framework import serializers

from .models import Ledger


class LedgerSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Ledger
        fields = ['data', 'quem', 'origem', 'valor']
