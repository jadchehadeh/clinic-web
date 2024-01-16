from django.shortcuts import render,redirect
from django.contrib import messages
from django.views import View
from patient.models import Patient
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate

def isUserNameUnique(username):
    return not User.objects.filter(username=username)
def isEmailUnique(email):
    return not User.objects.filter(email=email)

def isUserNameAndPasswordCorrect(username,password):
    return User.objects.filter(username=username,password=password)

class PatientLoginView(View):
    template_name = 'patient/login.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # Log the user in
            messages.success(request, f'Account logged in successfully for {username}')
            return redirect('patient-dashboard')  # Redirect to the patient dashboard or any desired URL
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('patient-login')  # Redirect back to the login page



class PatientSignUpView(View):
    template_name='patient/signup.html'
    def get(self,request):
        age=[]  #This loop is made for filling the list of ages from 1 to 99#
        for i in range(1,100):
            age.append(i)


        genders=['Male','Female']
        return render(request,self.template_name,{'gender':genders,'age':age})
    
    def post(self,request):
        username=request.POST['username']
        first_name=request.POST['firstname']
        last_name=request.POST['lastname']
        email=request.POST['email']
        phone=request.POST['phone']
        gender=request.POST['gender']
        place_of_residency=request.POST['place_of_residency']
        password=request.POST['password']
        emergency_number=request.POST['emergency_number']
        alergies=request.POST['alergies']
        age=request.POST['age']
        
        if isEmailUnique(email) and isUserNameUnique(username):
            user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
            user.save()

            patient=Patient.objects.create(user=user,phone=phone,gender=gender,place_of_residency=place_of_residency,emergency_number=emergency_number,alergies=alergies,age=age)
            messages.success(request,f'Account Created Successfully for {username}')
            return redirect('patient-login')
        else:
            messages.success(request,f'Email or UserName already Exists')
            return redirect('patient-signup')
            




    

            

    




