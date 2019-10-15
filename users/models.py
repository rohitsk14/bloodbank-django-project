from django.db import models
from django.contrib.auth.models import User

class profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=30,default="")
    mob_no = models.CharField(max_length=12,default="")
    age = models.CharField(max_length=5,default="")
    blood_group = models.CharField(default="",choices=(('A+','A+'),('B+','B+'),('A-','A-'),
                                                       ('B-','B-'),('O+','O+'),('O-','O-'),
                                                       ('AB+','AB+'),('AB-','AB-')),max_length=5)
    city = models.CharField(choices=(('MALEGAON','MALEGAON'),('NASHIK','NASHIK'),
                                     ('JALGAON','JALGAON'),('NAGAR','NAGAR')
                                     ,('MUMBAI','MUMBAI')),max_length=20)
    gender = models.CharField(max_length=10,default="",choices=(('MALE','MALE'),('FEMALE','FEMALE')))

    def __str__(self):
        return f'{self.user.username} profile'



class otp(models.Model):
    username = models.CharField(max_length=20,default="")
    email = models.EmailField(default="")
    password = models.CharField(max_length=50,default="")
    otp = models.IntegerField(default="")