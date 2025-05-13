from rest_framework import serializers

from smartphone.models import Manufacturers, Smartphone

class ManufacturerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Manufacturers
        fields = ['name','country_origin','date_of_fundation','website']

class SmartphoneSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Smartphone
        fields = ['manufacturers','name','ram','storage','screen_size']