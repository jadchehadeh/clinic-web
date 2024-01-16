from django.db import models
from django.contrib.auth.models import User

class Patient(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    phone=models.CharField(max_length=100)
    gender=models.CharField(max_length=10)
    place_of_residency=models.CharField(max_length=100)
    age=models.PositiveBigIntegerField(null=True)
    alergies=models.CharField(max_length=1000,null=True)
    emergency_number=models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.user.username

