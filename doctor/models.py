from django.db import models
from django.contrib.auth.models import User

class Doctor(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    specialization=models.CharField(max_length=100)
    number=models.CharField(max_length=100)
    experience=models.PositiveBigIntegerField()
    gender=models.CharField(max_length=20,null=True)
    residency=models.CharField(max_length=200,null=True)
    univrsity=models.CharField(max_length=200,null=True)


    def __str__(self):
        return self.user.username