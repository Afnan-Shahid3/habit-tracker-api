from django.shortcuts import render
from .serializer import HabitSerializer, HabitLogSerializer
from .models import Habit, HabitLog

from rest_framework import viewsets
from rest_framework.response import Response

from rest_framework.decorators import api_view, permission_classes, authentication_classes
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class HabitModelViewSet(viewsets.ModelViewSet):
    serializer_class = HabitSerializer

    def get_queryset(self):
        return Habit.objects.filter(user = self.request.user)

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)



class HabitLogModelViewSet(viewsets.ModelViewSet):
    serializer_class = HabitLogSerializer

    def get_queryset(self):
        return HabitLog.objects.filter(habitlogs__habits__user = self.request.user)


