from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.FileField()
    college = models.CharField(max_length=1000)
    course = models.CharField(max_length=100)
    specialisation = models.CharField(max_length=100)
    year = models.IntegerField()
    dob = models.IntegerField()
    phone_number = models.IntegerField()
    eyic_flag = models.BooleanField(default=False)
    eyrc_flag = models.BooleanField(default=False)
    eysip_flag = models.BooleanField(default=False)
    eystp_flag = models.BooleanField(default=False)
    eymooc_flag = models.BooleanField(default=False)
