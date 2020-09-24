from django.db import models
from orientations.models import Orientation

class Feedback(models.Model):
    # orientation = models.ForeignKey(Orientation, on_delete=models.CASCADE)
    name = models.CharField(max_length=500, blank=True)
    participant_type = models.CharField(max_length=10)
    college = models.CharField(max_length=1000)
    degree = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    year = models.IntegerField()
    email = models.EmailField(blank=True)
    orientation_rating = models.IntegerField()
    other_comments = models.CharField(max_length=1000)

    def __str__(self):
        return "TO ADD ORIENTATION" + " - " + str(self.orientation_rating)

