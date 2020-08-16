from rest_framework import serializers
from django.contrib.auth.models import User
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
    Low = serializers.FloatField()
    High = serializers.FloatField()

class CombineSerializers(serializers.Serializer):
    current = NiftySerializers()
    previous = NiftySerializers()
    year = YearSerializer(many=True)

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','password','email']

