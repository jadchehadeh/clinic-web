from django.urls import path,reverse_lazy
from patient.views.patientauth import PatientSignUpView,PatientLoginView
from django.contrib.auth.views import LoginView
urlpatterns=[

    path('signup/',PatientSignUpView.as_view(),name='patient-signup'),
    path('login/',PatientLoginView.as_view(),name='patient-login')
]