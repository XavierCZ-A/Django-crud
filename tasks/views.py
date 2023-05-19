from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login
from django.db import IntegrityError

def Tasks(request):
    return render(request, 'Tasks.html')

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
                return render('tasks')
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
