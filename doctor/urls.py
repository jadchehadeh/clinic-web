from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from doctor.views.doctorauth import doctorLogin as login,DoctorSignUpView as signup 
from doctor.views.dashboard import DashboardView,DoctorProfileView,viewAppointments,updateProfile


urlpatterns = [
 path('signup/',signup.as_view(),name='doctor-signup'),
 path('login/', LoginView.as_view(template_name='doctor/login.html'), name='doctor-login'),

  path('',DashboardView.as_view(),name='doctor-dashboard'),
  path('profile/',DoctorProfileView.as_view(),name='doctor-profile'),
 
 
  path('logout/',LogoutView.as_view(template_name='doctor/logout.html'),name='doctor-logout'),
  path('update/',updateProfile,name='update-profile'),
  path('appointment/',viewAppointments,name='doctor-appointment'),
  
  
   
    
    
]

