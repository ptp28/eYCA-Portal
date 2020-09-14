"""eyca/orientations
"""
from django.urls import path
from . import views
app_name = 'orientations'


urlpatterns = [
    path('add/', views.schedule_orientation, name="schedule_orientation"),
]
