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

@api_view(['POST'])
def login_api(request):
    try:

        data = request.data
        username = data.get('username')
        password = data.get('password')
        user = authenticate(username = username, password = password)
        if user:
            token = Token.objects.get_or_create(user = user)
            return Response({'status' : 200, 'token' : str(token)})

        return Response({'status' : 300, 'message' : "Invalid Credentials"})

    except Exception as e:
        print(e)
    return Response({
        'status' : 400,
        'message': "Something went wrong"
    })


class HabitModelViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    
    serializer_class = HabitSerializer

    def get_queryset(self):
        return Habit.objects.filter(user = self.request.user)

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)



class HabitLogModelViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = HabitLogSerializer

    def get_queryset(self):
        return HabitLog.objects.filter(habit__user = self.request.user)


