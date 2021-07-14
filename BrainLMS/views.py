from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import *


def index(request, *args, **kwargs):
    return render(request, 'BrainLMS/index.html')

@unauthenticated_user
def userSignUp(request, *args, **kwargs):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user_type = request.POST['user_type']

        if first_name and last_name and username and email and password:
            user = User.objects.create_user(email=email, username=username, first_name=first_name, last_name=last_name, password=password)

            if user:
                group = Group.objects.get(name=user_type)
                user.groups.add(group)
            return redirect(index)
    return render(request, 'BrainLMS/signup.html')

@unauthenticated_user
def userLogin(request, *args, **kwargs):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, username=username,  email=email, password=password)

        if user is not None:
            print("login trying")
            login(request, user)
            print("login successful")
            return redirect(index)

    return render(request, 'BrainLMS/login.html')

@login_required(login_url='/login/')
def logOut(request, *args, **kwargs):
    logout(request)
    return redirect(userLogin)