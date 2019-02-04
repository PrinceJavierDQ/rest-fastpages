from .models import Client
from rest_framework import viewsets
from .serializers import ClientSerializer

# Create your views here.


class ClientViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows clients to be viewed or edited.
    """
    queryset = Client.objects.all().order_by('-paid_until')
    serializer_class = ClientSerializer

