from django.urls import path
from . import views

urlpatterns = [
    # ... other URL patterns
    path('recognize_speech/', views.recognize_speech, name='recognize_speech'),
]
