from django.db import models
from orientations.models import Orientation

class Feedback(models.Model):
    orientation = models.ForeignKey(Orientation, on_delete=models.CASCADE)
    name = models.CharField(max_length=500, blank=True)
    student = models.BooleanField(default=True)
    course = models.CharField(max_length=100)
    specialisation = models.CharField(max_length=100)
    year = models.IntegerField()
    email_id = models.EmailField(blank=True)
    orientation_rating = models.IntegerField()
    other_comments = models.CharField(max_length=1000)

