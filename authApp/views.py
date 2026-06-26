from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from authApp.models import UserProfile as User
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages
# Create your views here.

def home_view(request):
    return render(request, 'index.html')

def about_view(request):
    return render(request, 'authApp/about.html')

def login_view(request):
    if request.method == 'POST':
        loginUsername = request.POST['loginusername'].strip()
        loginPassword = request.POST['loginpassword'].strip()
        print(f'Debugging Inputs: ---> UserName:{loginUsername}  Password--->{loginPassword}')
        
        if ((not loginUsername) or (not loginPassword)):
            print('No user found:')
        else:
            
            user = authenticate(username=loginUsername, password=loginPassword)
            print(f'Debugging Result: ---> {user}')
            if user is not None: 
                login(request, user)
                print('User is authenticated:')
                messages.success(request, "Login Successfull:")
                return redirect('home')
            else:
                return render(request, 'authApp/signin.html')
    return render(request, 'authApp/signin.html')

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstName = request.POST['fName']
        lastName = request.POST['lName']
        email = request.POST['email']
        contactNumber = request.POST['contactNumber']
        passwordOne = request.POST['pass1']
        passwordTwo = request.POST['pass2']
        if ((firstName) and (lastName) and (email) and (contactNumber)):
            print('Data is getting saved inside the database:')
        if ((passwordOne == passwordTwo) and (len(passwordOne) >= 8) and (len(passwordTwo) >= 8)):
            # Getting the password secured..
            hashed_password = make_password(passwordOne)
            
            # Saving data
            new_user = User.objects.create(username=username, email=email, contactNumber=contactNumber, password=hashed_password)
            
            new_user.save(); # Saved the User in the database:
            
            if(new_user):
                print('Data Saved Successfully:')
            else:
                print('Some errors')   
    return render(request, 'authApp/signup.html')