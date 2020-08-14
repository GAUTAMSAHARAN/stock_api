from rest_framework import serializers
from stock import models

class AshokleySerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Ashokley
        fields = '__all__'

class SensexSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Sensex
        fields = "__all__"
    
class CiplaSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Cipla
        fields = "__all__"
    
class NiftySerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Nifty
        fields = "__all__"
    
class RelianceSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Reliance
        fields = "__all__"
    
class TatasteelSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Tatasteel
        fields = "__all__"

class EichermotorsSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Eichermotors
        fields = "__all__"

class YearSerializer(serializers.Serializer):
    year = serializers.IntegerField()


class CombineSerializers(serializers.Serializer):
    current = NiftySerializers()
    previous = NiftySerializers()
