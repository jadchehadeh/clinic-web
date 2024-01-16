from django.db import models
from patient.models import Patient  
from doctor.models import Doctor

class MedicalRecord(models.Model):
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    date=models.DateField()
    diagnosis=models.CharField(max_length=1000)
    treatment=models.CharField(max_length=1000)
    test_result=models.CharField(max_length=1000)
    doctor_notes=models.CharField(max_length=1000)


# Create your models here.
