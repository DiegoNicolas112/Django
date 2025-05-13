from rest_framework import viewsets
from smartphone.models import Manufacturers, Smartphone
from smartphone.serializers import ManufacturerSerializer, SmartphoneSerializer

class ManufacturerViewSet(viewsets.ModelViewSet):
    queryset = Manufacturers.objects.all()
    serializer_class = ManufacturerSerializer

class SmartphoneViewSet(viewsets.ModelViewSet):
    queryset = Smartphone.objects.all()
    serializer_class = SmartphoneSerializer