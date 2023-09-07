from .views import api_endpoint
from django.urls import path
# from django.

urlpatterns = [
    path('api/', api_endpoint, name="endpoint"),
    
] 