import requests
from django.shortcuts import render
import django_filters
from psycopg2.extras import DateRange
from stock import models
from rest_framework import generics, request ,mixins
from rest_framework.response import Response
from stock import serializers
from rest_framework import viewsets
from rest_framework.decorators import action
from collections import namedtuple
from datetime import datetime, timedelta
from django.db.models import Avg, Max, Min, Sum


Combine = namedtuple('Combine', ('current', 'previous'))
particular_date = datetime(2020, 8, 13)
previous_date = particular_date - timedelta(days = 1)
starting_date = particular_date - timedelta(days=365)


# Create your views here.
class AshokleyViewSet(viewsets.ModelViewSet):
    queryset = models.Ashokley.objects.all()
    serializer_class = serializers.AshokleySerializers


    @action(methods=['get',], detail=False, url_path='day', url_name='day')
    def get_day(self, request):
        particular_date = datetime(2020, 8, 13)
        data = models.Ashokley.objects.filter(Low == 1000)
        serialized = serializers.AshokleySerializers(data)
        return Response(serialized.data)

class SensexViewSet(viewsets.ModelViewSet):
    queryset = models.Sensex.objects.all()
    serializer_class = serializers.SensexSerializers



    @action(methods=['get', ], detail=False, url_path='data', url_name='data')
    def get_sensex(self, request):
        data = models.Sensex.objects.filter(Date__gte = starting_date)
        results = serializers.SensexSerializers(data, many = True)
        year_high =  data.aggregate(Max('High'))
        year_low = data.aggregate(Min('Low'))
        current_data = models.Sensex.objects.get(Date = particular_date)
        previous_data = models.Sensex.objects.get(Date = previous_date)
        combine = Combine(
            current=current_data,
            previous=previous_data,
        )
        serializer = serializers.CombineSerializers(combine)
        return Response(serializer.data)

class CiplaViewSet(viewsets.ModelViewSet):
    queryset = models.Cipla.objects.all()
    serializer_class = serializers.CiplaSerializers

class NiftyViewSet(viewsets.ModelViewSet):
    queryset = models.Nifty.objects.all()
    serializer_class = serializers.NiftySerializers


    @action(methods=['get', ], detail=False, url_path='niftydata', url_name='niftydata')
    def get_nifty(self, request):
        data = models.Nifty.objects.filter(DateRange(Date, particular_date))
        year_high =  data.objects.all().aggregate(Max('High'))
        year_low = data.objects.all().aggregate(Min('Low'))
        current_data = models.Nifty.objects.filter(Date == particular_date)
        previous_data = models.Nifty.objects.filter(Date == previous_data )
        combine = Combine(
            current=current_data,
            previous=previous_data,
            year_low=year_low,
            year_high=year_high,
        )
        serializer = serializers.CombineSerializers(combine)
        return Response(serializer.data)



class RelianceViewSet(viewsets.ModelViewSet):
    queryset = models.Reliance.objects.all()
    serializer_class = serializers.RelianceSerializers

class TatasteelViewSet(viewsets.ModelViewSet):
    queryset = models.Tatasteel.objects.all()
    serializer_class = serializers.RelianceSerializers

class EichermotorsViewSet(viewsets.ModelViewSet):
    queryset = models.Eichermotors.objects.all()
    serializer_class = serializers.RelianceSerializers
