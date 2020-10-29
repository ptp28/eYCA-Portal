from django.db import models


class Registration(models.Model):
    name = models.CharField(max_length=500)
    email = models.EmailField()
    username = models.CharField(max_length=100)
    profile_pic = models.FileField()
    college = models.CharField(max_length=1000)
    course = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    year = models.IntegerField()
    dob = models.IntegerField()
    phone_number = models.IntegerField()
    id_card_pic = models.FileField()
    eyic_flag = models.BooleanField(default=False)
    eyrc_flag = models.BooleanField(default=False)
    eysip_flag = models.BooleanField(default=False)
    eystp_flag = models.BooleanField(default=False)
    eymooc_flag = models.BooleanField(default=False)
    approve_registration = models.BooleanField(default=False)

    def __str__(self):
        return self.name + " - " + self.username


