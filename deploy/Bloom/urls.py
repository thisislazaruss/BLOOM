from django.urls import path
from .views import success

urlpatterns = [
    path('success/', success, name="success"),
    
]