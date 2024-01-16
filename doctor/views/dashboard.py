from typing import Any
from django.db import models
from django.shortcuts import redirect,render,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin#login required mixin is used to prevent user from changing the url menually without registring so i manage to redirect them into the login page
from doctor.models import Doctor
from django.contrib.auth.models import User

class DashboardView(LoginRequiredMixin,DetailView):#This View Responsible for displaying the Doctor Dashboard with the current Logged in user data, also this view can't be accessed until the doctor is logged in
    model=Doctor
    login_url='/doctor/login'
    template_name='doctor/dashboard.html'
    context_object_name="doctor"
   
    
    def get_object(self, queryset=None):
        user = self.request.user
        return get_object_or_404(Doctor, user=user)



class DoctorProfileView(LoginRequiredMixin,DetailView):#This View Responsible for the displaying the profile of the doctor in case if he want to change his profile
    login_url = '/doctor/login'  # Django will redirect un registerd user to to the login page
    model = Doctor
    template_name = 'doctor/profile.html'
    context_object_name = 'doctor'
    specialization = ["Cardiologist", "Dermatologist", "Gastroenterologist", "Pediatrician", "Ophthalmologist"]#this list is passed to the view to fill the form with doctor specilizations after that inside the template i made a if condition to get the current doctor specializations among those incase he want to change.
    def get_object(self, queryset=None):
        user = self.request.user
        return get_object_or_404(Doctor, user=user)
    
    def get_context_data(self, **kwargs):   #this function is used to send context to template by overriding the get_context_Data function from the DetailView Class
        context = super().get_context_data(**kwargs)
        context['specialization'] = self.specialization
        return context
    
def updateProfile(request):#Here i uses function based view because if we need to update a model using a generic update view that can uses forms.py but as our objective is to not use ready forms by django
    if request.method == 'POST':
        doctor_id = request.POST.get('doctor_id')
        doctor = get_object_or_404(Doctor, id=doctor_id)
        doctor.specialization=request.POST.get('Specialization')
        doctor.experience=request.POST.get('experience')
        doctor.number=request.POST.get('phone')
        user_id = request.POST.get('user_id')
        user = get_object_or_404(User, id=user_id)
        user.first_name = request.POST.get('firstname')
        user.last_name = request.POST.get('lastname')
       
        user.save()  # Save the user object
        doctor.save()

        return redirect('/doctor/profile?message=Profile+updated+successfully')

def viewAppointments(request):
    user=request.user
    doctor=get_object_or_404(Doctor,user=user)


    return render(request,'doctor/appointment.html',{'doctor':doctor})


