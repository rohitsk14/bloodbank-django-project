from django.db import models


class requests(models.Model):
    name = models.CharField(max_length=30,default="")
    hospital_name = models.CharField(max_length=30,default="")
    blood_group = models.CharField(max_length=10)
    city = models.CharField(max_length=30)
    mobile_no = models.CharField(max_length=12,default="")

class messages(models.Model):
    name = models.CharField(max_length=30)
    message = models.TextField()
    email = models.EmailField()