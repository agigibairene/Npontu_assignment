from django.urls import path
from .views import HealthCheck


urlpatterns = [
    path('health_check/', HealthCheck.as_view())
]