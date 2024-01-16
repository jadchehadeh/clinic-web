from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.views import View
from doctor.models import Doctor


def isUsernameUnique(username): #this function will check if the username is already exists in database#
    return not User.objects.filter(username=username).exists()
def isEmailUnique(email):
    return not User.objects.filter(email=email).exists()

class DoctorSignUpView(View):
    template_name = 'doctor/signup.html'

    def get(self, request):
        msg = ''
        specialization_list = ["Cardiologist", "Dermatologist", "Gastroenterologist", "Pediatrician", "Ophthalmologist"]
        context = {
            'msg': msg,
            'specialization_list': specialization_list,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        msg = ''
       
        
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        specialization = request.POST['Specialization']
        email = request.POST['email']
        password = request.POST['password']
        experience = request.POST['experience']
        number = request.POST['phone']

        if isEmailUnique(email) and isUsernameUnique(username):
            user = User.objects.create_user(username=username, first_name=firstname, last_name=lastname, email=email, password=password)
            
            doctor = Doctor.objects.create(specialization=specialization, number=number, experience=experience, user=user)
            messages.success(request,f'Account created for {username}! you are now able to login')
            return redirect("doctor-login")
        else:
            msg = "Username or email is not unique."
            messages.success(request,f'Email or UserName Already Exists')
            return redirect("doctor-signup")

        context = {
            'msg': msg,
            
        }
        return render(request, self.template_name, context)



def doctorLogin(request):
    return render(request,'doctor/login.html')




