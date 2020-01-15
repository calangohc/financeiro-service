from dashboard.models import Registros
from rest_framework import viewsets
from .serializers import RegistrosSerializer


class RegistrosViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Registros.objects.all()
    serializer_class = RegistrosSerializer
