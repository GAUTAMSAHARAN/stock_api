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
from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework.authtoken.models import Token

Combine = namedtuple('Combine', ('current', 'previous', 'year'))
particular_date = datetime(2020, 8, 13)
previous_date = particular_date - timedelta(days = 1)
starting_date = particular_date - timedelta(days=365)


# Create your views here.
class AshokleyViewSet(viewsets.ModelViewSet):
    queryset = models.Ashokley.objects.all()
    serializer_class = serializers.AshokleySerializers

    @action(methods=['get',], detail=False, url_path='day', url_name='day')
    def get_day(self, request):
        data = models.Ashokley.objects.get(Date = particular_date)
        serialized = serializers.AshokleySerializers(data)
        return Response(serialized.data)
    
    @action(methods=['get',], detail=False, url_path='week', url_name='week')
    def get_week(self, request):
        data = models.Ashokley.objects.filter(Date__gte = particular_date-timedelta(days=7))
        serialized = serializers.AshokleySerializers(data, many=True)
        return Response(serialized.data)
    
    @action(methods=['get',], detail=False, url_path='month', url_name='month')
    def get_month(self, request):
        data = models.Ashokley.objects.filter(Date__gte = particular_date-timedelta(days=30))
        serialized = serializers.AshokleySerializers(data, many=True)
        return Response(serialized.data)

    @action(methods=['get',], detail=False, url_path='threemonth', url_name='threemonth')
    def get_three_month(self, request):
        data = models.Ashokley.objects.filter(Date__gte = particular_date-timedelta(days=90))
        serialized = serializers.AshokleySerializers(data, many=True)
        return Response(serialized.data)

    @action(methods=['get',], detail=False, url_path='sixmonth', url_name='sixmonth')
    def get_six_month(self, request):
        data = models.Ashokley.objects.filter(Date__gte = particular_date-timedelta(days=180))
        serialized = serializers.AshokleySerializers(data, many=True)
        return Response(serialized.data)

    @action(methods=['get',], detail=False, url_path='year', url_name='year')
    def get_year(self, request):
        data = models.Ashokley.objects.filter(Date__gte = particular_date-timedelta(days=365))
        serialized = serializers.AshokleySerializers(data, many=True)
        return Response(serialized.data)

    @action(methods=['get',], detail=False, url_path='fiveyear', url_name='fiveyear')
    def get_five_year(self, request):
        data = models.Ashokley.objects.filter(Date__gte = particular_date-timedelta(days=1825))
        serialized = serializers.AshokleySerializers(data, many=True)
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
        year = [{'Low': year_low.get('Low__min'), 'High': year_high.get('High__max')}]
        combine = Combine(
            current=current_data,
            previous=previous_data,
            year=year,
        )
        serializer = serializers.CombineSerializers(combine)
        return Response(serializer.data)

class CiplaViewSet(viewsets.ModelViewSet):
    queryset = models.Cipla.objects.all()
    serializer_class = serializers.CiplaSerializers

    @action(methods=['get',], detail=False, url_path='day', url_name='day')
    def get_day(self, request):
        data = models.Cipla.objects.get(Date = particular_date)
        serialized = serializers.AshokleySerializers(data)
        return Response(serialized.data)
    
    @action(methods=['get',], detail=False, url_path='week', url_name='week')
    def get_week(self, request):
        data = models.Cipla.objects.filter(Date__gte = particular_date-timedelta(days=7))
        serialized = serializers.AshokleySerializers(data, many=True)
        return Response(serialized.data)
    
    @action(methods=['get',], detail=False, url_path='month', url_name='month')
    def get_month(self, request):
        data = models.Cipla.objects.filter(Date__gte = particular_date-timedelta(days=30))
        serialized = serializers.AshokleySerializers(data, many=True)
        return Response(serialized.data)

    @action(methods=['get',], detail=False, url_path='threemonth', url_name='threemonth')
    def get_three_month(self, request):
        data = models.Cipla.objects.filter(Date__gte = particular_date-timedelta(days=90))
        serialized = serializers.AshokleySerializers(data, many=True)
        return Response(serialized.data)

    @action(methods=['get',], detail=False, url_path='sixmonth', url_name='sixmonth')
    def get_six_month(self, request):
        data = models.Cipla.objects.filter(Date__gte = particular_date-timedelta(days=180))
        serialized = serializers.AshokleySerializers(data, many=True)
        return Response(serialized.data)

    @action(methods=['get',], detail=False, url_path='year', url_name='year')
    def get_year(self, request):
        data = models.Cipla.objects.filter(Date__gte = particular_date-timedelta(days=365))
        serialized = serializers.AshokleySerializers(data, many=True)
        return Response(serialized.data)

    @action(methods=['get',], detail=False, url_path='fiveyear', url_name='fiveyear')
    def get_five_year(self, request):
        data = models.Cipla.objects.filter(Date__gte = particular_date-timedelta(days=1825))
        serialized = serializers.AshokleySerializers(data, many=True)
        return Response(serialized.data)

class NiftyViewSet(viewsets.ModelViewSet):
    queryset = models.Nifty.objects.all()
    serializer_class = serializers.NiftySerializers

    @action(methods=['get', ], detail=False, url_path='niftydata', url_name='niftydata')
    def get_nifty(self, request):
        data = models.Nifty.objects.filter(Date__gte = starting_date)
        results = serializers.NiftySerializers(data, many = True)
        year_high =  data.aggregate(Max('High'))
        year_low = data.aggregate(Min('Low'))
        current_data = models. Nifty.objects.get(Date = particular_date)
        previous_data = models.Nifty.objects.get(Date = previous_date)
        year = [{'Low': year_low.get('Low__min'), 'High': year_high.get('High__max')}]
        combine = Combine(
            current=current_data,
            previous=previous_data,
            year=year,
        )
        serializer = serializers.CombineSerializers(combine)
        return Response(serializer.data)



class RelianceViewSet(viewsets.ModelViewSet):
    queryset = models.Reliance.objects.all()
    serializer_class = serializers.RelianceSerializers

    @action(methods=['get',], detail=False, url_path='day', url_name='day')
    def get_day(self, request):
        data = models.Reliance.objects.get(Date = particular_date)
        serialized = serializers.AshokleySerializers(data)
        return Response(serialized.data)
    
    @action(methods=['get',], detail=False, url_path='week', url_name='week')
    def get_week(self, request):
        data = models.Reliance.objects.filter(Date__gte = particular_date-timedelta(days=7))
        serialized = serializers.AshokleySerializers(data, many=True)
        return Response(serialized.data)
    
    @action(methods=['get',], detail=False, url_path='month', url_name='month')
    def get_month(self, request):
        data = models.Reliance.objects.filter(Date__gte = particular_date-timedelta(days=30))
        serialized = serializers.AshokleySerializers(data, many=True)
        return Response(serialized.data)

    @action(methods=['get',], detail=False, url_path='threemonth', url_name='threemonth')
    def get_three_month(self, request):
        data = models.Reliance.objects.filter(Date__gte = particular_date-timedelta(days=90))
        serialized = serializers.AshokleySerializers(data, many=True)
        return Response(serialized.data)

    @action(methods=['get',], detail=False, url_path='sixmonth', url_name='sixmonth')
    def get_six_month(self, request):
        data = models.Reliance.objects.filter(Date__gte = particular_date-timedelta(days=180))
        serialized = serializers.AshokleySerializers(data, many=True)
        return Response(serialized.data)

    @action(methods=['get',], detail=False, url_path='year', url_name='year')
    def get_year(self, request):
        data = models.Reliance.objects.filter(Date__gte = particular_date-timedelta(days=365))
        serialized = serializers.AshokleySerializers(data, many=True)
        return Response(serialized.data)

    @action(methods=['get',], detail=False, url_path='fiveyear', url_name='fiveyear')
    def get_five_year(self, request):
        data = models.Reliance.objects.filter(Date__gte = particular_date-timedelta(days=1825))
        serialized = serializers.AshokleySerializers(data, many=True)
        return Response(serialized.data)

class TatasteelViewSet(viewsets.ModelViewSet):
    queryset = models.Tatasteel.objects.all()
    serializer_class = serializers.RelianceSerializers

    @action(methods=['get',], detail=False, url_path='day', url_name='day')
    def get_day(self, request):
        data = models.Tatasteel.objects.get(Date = particular_date)
        serialized = serializers.AshokleySerializers(data)
        return Response(serialized.data)
    
    @action(methods=['get',], detail=False, url_path='week', url_name='week')
    def get_week(self, request):
        data = models.Tatasteel.objects.filter(Date__gte = particular_date-timedelta(days=7))
        serialized = serializers.AshokleySerializers(data, many=True)
        return Response(serialized.data)
    
    @action(methods=['get',], detail=False, url_path='month', url_name='month')
    def get_month(self, request):
        data = models.Tatasteel.objects.filter(Date__gte = particular_date-timedelta(days=30))
        serialized = serializers.AshokleySerializers(data, many=True)
        return Response(serialized.data)

    @action(methods=['get',], detail=False, url_path='threemonth', url_name='threemonth')
    def get_three_month(self, request):
        data = models.Tatasteel.objects.filter(Date__gte = particular_date-timedelta(days=90))
        serialized = serializers.AshokleySerializers(data, many=True)
        return Response(serialized.data)

    @action(methods=['get',], detail=False, url_path='sixmonth', url_name='sixmonth')
    def get_six_month(self, request):
        data = models.Tatasteel.objects.filter(Date__gte = particular_date-timedelta(days=180))
        serialized = serializers.AshokleySerializers(data, many=True)
        return Response(serialized.data)

    @action(methods=['get',], detail=False, url_path='year', url_name='year')
    def get_year(self, request):
        data = models.Tatasteel.objects.filter(Date__gte = particular_date-timedelta(days=365))
        serialized = serializers.AshokleySerializers(data, many=True)
        return Response(serialized.data)

    @action(methods=['get',], detail=False, url_path='fiveyear', url_name='fiveyear')
    def get_five_year(self, request):
        data = models.Tatasteel.objects.filter(Date__gte = particular_date-timedelta(days=1825))
        serialized = serializers.AshokleySerializers(data, many=True)
        return Response(serialized.data)

class EichermotorsViewSet(viewsets.ModelViewSet):
    queryset = models.Eichermotors.objects.all()
    serializer_class = serializers.RelianceSerializers

    @action(methods=['get',], detail=False, url_path='day', url_name='day')
    def get_day(self, request):
        data = models.Eichermotors.objects.get(Date = particular_date)
        serialized = serializers.AshokleySerializers(data)
        return Response(serialized.data)
    
    @action(methods=['get',], detail=False, url_path='week', url_name='week')
    def get_week(self, request):
        data = models.Eichermotors.objects.filter(Date__gte = particular_date-timedelta(days=7))
        serialized = serializers.AshokleySerializers(data, many=True)
        return Response(serialized.data)
    
    @action(methods=['get',], detail=False, url_path='month', url_name='month')
    def get_month(self, request):
        data = models.Eichermotors.objects.filter(Date__gte = particular_date-timedelta(days=30))
        serialized = serializers.AshokleySerializers(data, many=True)
        return Response(serialized.data)

    @action(methods=['get',], detail=False, url_path='threemonth', url_name='threemonth')
    def get_three_month(self, request):
        data = models.Eichermotors.objects.filter(Date__gte = particular_date-timedelta(days=90))
        serialized = serializers.AshokleySerializers(data, many=True)
        return Response(serialized.data)

    @action(methods=['get',], detail=False, url_path='sixmonth', url_name='sixmonth')
    def get_six_month(self, request):
        data = models.Eichermotors.objects.filter(Date__gte = particular_date-timedelta(days=180))
        serialized = serializers.AshokleySerializers(data, many=True)
        return Response(serialized.data)

    @action(methods=['get',], detail=False, url_path='year', url_name='year')
    def get_year(self, request):
        data = models.Eichermotors.objects.filter(Date__gte = particular_date-timedelta(days=365))
        serialized = serializers.AshokleySerializers(data, many=True)
        return Response(serialized.data)

    @action(methods=['get',], detail=False, url_path='fiveyear', url_name='fiveyear')
    def get_five_year(self, request):
        data = models.Eichermotors.objects.filter(Date__gte = particular_date-timedelta(days=1825))
        serialized = serializers.AshokleySerializers(data, many=True)
        return Response(serialized.data)

class UserView(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class = serializers.UserSerializers
    
    def create(self, request):
        try:
            user = User.objects.get(email=request.data['email'])
            if user:
                return Response("user with current email already exists")
        except User.DoesNotExist:
            user = User(email=request.data['email'],username=request.data['username'],first_name=request.data['first_name'],password=request.data['password'])
            user.save()

        try:
            token = Token.objects.get(user=user)
        except Token.DoesNotExist:
            token = Token.objects.create(user=user)

        res = {
            "token": token.key,
            "user_data": serializers.UserSerializers(user).data
        }
        return JsonResponse(res)
    
    @action(methods=['post'],detail=False,url_name='login',url_path='login')
    def login(self,request):
        try:
            user = User.objects.get(email=request.data['email'],password=request.data['password'])
            try:
                token = Token.objects.get(user=user)
            except Token.DoesNotExist:
                token = Token.objects.create(user=user)
            
            res = {
                "token":token.key,
                "user_data":serializers.UserSerializers(user).data
            }
            return JsonResponse(res)
        except User.DoesNotExist:
            return Response("your username or password is incorrect")