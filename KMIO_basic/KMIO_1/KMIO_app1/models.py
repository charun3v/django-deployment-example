from django.db import models

#import basic user model: for user profile
from django.contrib.auth.models import User


class PatientID(models.Model):
    Mr_No = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return str(self.Mr_No)


class PatientName(models.Model):
    category = models.ForeignKey(PatientID, on_delete=models.DO_NOTHING)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name


class PatientAge(models.Model):
    cat = models.ForeignKey(PatientID, on_delete=models.DO_NOTHING)
    age = models.FloatField

    def __str__(self):
        return str(self.age)
# Create your models here.

#class for the user profile info


class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
        #model class to add additional info which default user does not have (like - name, emai, text in the forms.py)

    #additional classes
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username
                #username is the default attribute of the 'User'