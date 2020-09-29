from django.db import models


class Orientation(models.Model):
    about = models.CharField(max_length=500)
    date = models.DateField()
    time_from = models.TimeField()
    time_till = models.TimeField()
    meeting_type = models.CharField(max_length=100)
    expected_participants = models.IntegerField()
    outreach = models.BooleanField(default=False)
    status = models.CharField(max_length=50, default="Scheduled")

    def __str__(self):
        return str(self.date) + " - " + "TO ADD CA NAME TO STRING"


class OrientationReport(models.Model):
    orientation = models.ForeignKey(Orientation, on_delete=models.CASCADE)
    num_participants = models.IntegerField()
    activities_description = models.CharField(max_length=1000)
    activities_photo = models.FileField()
    other_attachments = models.FileField(blank=True)