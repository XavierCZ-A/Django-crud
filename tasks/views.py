from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login,logout, authenticate
from django.db import IntegrityError

def Tasks(request):
    return render(request, 'Tasks.html')


def Home(request):
    return render(request, 'Home.html')

def Signout(request):
    logout(request)
    return redirect('home')

def Signup(request):
    if request.method == 'GET':
        return render(request, 'Signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return render(request, 'Tasks.html')
            #para validar como usuarios ya creados en la BD con integrity
            except IntegrityError:
                return render(request, 'Signup.html', {
                    'form': UserCreationForm,
                    'error': 'User already exists'
                })
        return render(request, 'Signup.html', {
                'form': UserCreationForm,
                'error': 'Password do not match'
            })

def Signin(request):
    # if request.method == 'GET':
    #     return render(request, 'Signin.html', {
    #         'form': AuthenticationForm,
    #         'error': 'error singin'
    #     })
    # else:
    #     print(request.POST)
    #     return render(request, 'Signin.html', {
    #         'form': AuthenticationForm,
    #     })
    if request.method == 'GET':
        return render(request, 'signin.html', {"form": AuthenticationForm})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {"form": AuthenticationForm, "error": "Username or password is incorrect."})

        login(request, user)
        return redirect('tasks')

