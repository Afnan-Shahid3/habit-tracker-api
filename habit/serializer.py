from rest_framework import serializers
from .models import Habit, HabitLog

class HabitSerializer(serializers.Serializer):
    class meta:
        model = Habit
        fields = ['id', 'name', 'frequency', 'created_at']

class HabitLogSerializer(serializers.Serializer):
    class meta:
        model = HabitLog
        fields = ['id', 'habit', 'date', 'completed']
        