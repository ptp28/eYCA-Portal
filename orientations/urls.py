"""eyca/orientations
"""
from django.urls import path
from . import views
app_name = 'orientations'


urlpatterns = [
    path('add/', views.schedule_orientation, name="schedule_orientation"),
    path('report/', views.orientation_report, name="orientation_report")
]
