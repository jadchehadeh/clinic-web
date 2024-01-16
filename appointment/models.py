from django.db import models
from doctor.models import Doctor
from django.contrib.auth.models import User
from patient.models import Patient

class Appointment(models.Model):
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    date=models.DateField()
    time=models.TimeField()
    status=models.CharField(max_length=100)
    appointment_type=models.CharField(max_length=100)
    prescription=models.CharField(max_length=100)
    cancelation_reason=models.CharField(max_length=1000)
    

# Create your models here.
