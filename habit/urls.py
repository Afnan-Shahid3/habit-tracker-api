from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register('habits', views.HabitModelViewSet, basename = 'habits')
router.register('habitlogs', views.HabitLogModelViewSet, basename = 'habitlogs')

urlpatterns = [
    path('api/', include(router.urls)),
    path('login/', views.login_api)
]