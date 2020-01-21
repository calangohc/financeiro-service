from ledger.models import Ledger
from rest_framework import serializers


class LedgerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ledger
        fields = ['data', 'quem', 'origem', 'valor']
