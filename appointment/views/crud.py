from django.shortcuts import render

def signup(request):
    return render(request,'crud/signup.html')

def login(request):
    return render(request,'crud/login.html')
