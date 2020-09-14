from django.db import models


class Orientation(models.Model):
    about = models.CharField(max_length=500)
    date = models.DateField()
    time = models.TimeField()
    meeting_type = models.CharField(max_length=100)
    expected_participants = models.IntegerField()
    outreach = models.BooleanField(default=False)
    status = models.CharField(max_length=50, default="Scheduled")


class OrientationReport(models.Model):
    orientation = models.ForeignKey(Orientation, on_delete=models.CASCADE)
    num_participants = models.IntegerField()
    activities_description = models.CharField(max_length=1000)
    activities_photo = models.FileField()
    other_attachments = models.FileField(blank=True)


# class QuarterlyReport(models.Model):
#     month = models.IntegerField()
#     year = models.IntegerField()
#     month_flag = models.IntegerField()
#     report = models.FileField(null=True, blank=True)
#     comment = models.CharField(max_length=200, null=True)
#     timestamp = models.DateTimeField(auto_now=True)
