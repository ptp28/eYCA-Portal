"""eyca/feedback
"""
from django.urls import path
from . import views


app_name = 'feedback'

urlpatterns = [
    path('', views.orientations_list, name="orientations_list"),
    path('<int:orientation_id>/', views.feedback_submit, name="feedback_submit"),

]
