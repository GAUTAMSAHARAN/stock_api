from django.shortcuts import render
from stock import models
from stock import serializers
from rest_framework import viewsets

# Create your views here.
class AshokleyViewSet(viewsets.ModelViewSet):
    queryset = models.Ashokley.objects.all()
    serializer_class = serializers.AshokleySerializers

class SensexViewSet(viewsets.ModelViewSet):
    queryset = models.Sensex.objects.all()
    serializer_class = serializers.SensexSerializers

class CiplaViewSet(viewsets.ModelViewSet):
    queryset = models.Cipla.objects.all()
    serializer_class = serializers.CiplaSerializers

class NiftyViewSet(viewsets.ModelViewSet):
    queryset = models.Nifty.objects.all()
    serializer_class = serializers.NiftySerializers

class RelianceViewSet(viewsets.ModelViewSet):
    queryset = models.Reliance.objects.all()
    serializer_class = serializers.RelianceSerializers

class TatasteelViewSet(viewsets.ModelViewSet):
    queryset = models.Tatasteel.objects.all()
    serializer_class = serializers.RelianceSerializers

class EichermotorsViewSet(viewsets.ModelViewSet):
    queryset = models.Eichermotors.objects.all()
    serializer_class = serializers.RelianceSerializers
