from rest_framework import serializers
from .models import Habit, HabitLog

class HabitLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = HabitLog
        fields = ['id', 'habit', 'date', 'completed']
        
    
class HabitSerializer(serializers.ModelSerializer):
    
    habitlogs = HabitLogSerializer(many = True, read_only= True)

    class Meta:
        model = Habit
        fields = ['id', 'name', 'frequency', 'created_at', 'habitlogs']
