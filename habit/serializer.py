from rest_framework import serializers
from .models import Habit, HabitLog

class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = ['id', 'name', 'frequency', 'created_at']

class HabitLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = HabitLog
        fields = ['id', 'habit', 'date', 'completed']
        