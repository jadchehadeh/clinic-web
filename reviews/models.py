from django.db import models
from patient.models import Patient
from doctor.models import Doctor

class Review(models.Model):
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    review=models.CharField(max_length=1000)
    notes=models.CharField(max_length=1000)
    

# Create your models here.
