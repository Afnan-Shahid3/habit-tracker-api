from django.db import models
from django.contrib.auth.models import User 
# Create your models here.
class Habit(models.Model):
    CHOICES = [
        ('daily', 'Daily'),
        ('weekly', "Weekly"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'habits')
    name = models.CharField(max_length=255)
    frequency = models.CharField(max_length=10, choices=CHOICES)
    created_at = models.DateTimeField(auto_now= True)


class HabitLog(models.Model):
    habit = models.ForeignKey(Habit, on_delete= models.CASCADE, related_name = 'habitlogs')
    date = models.DateField()
    completed = models.BooleanField(default=False)

    class Meta:
        unique_together = ('habit', 'date')
