# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import User
from django.contrib import messages
from django.contrib.messages import error
from django.shortcuts import render, HttpResponse, redirect
def index(request):
    if 'name' in request.session:
        return redirect('/dashboard')

    return render(request, 'friends/index.html')

def create(request):
    errors = User.objects.validate(request.POST)
    if len(errors):
        for field, message in errors.iteritems():
            error(request, message, extra_tags=field)

        return redirect('/')

    if request.method == "POST":
        var1 = request.POST['password']
        var2 = request.POST['confirm']

    if var1 == var2:
        User.objects.create(
            name = request.POST['name'],
            username = request.POST['username'],
            email = request.POST['email'],
            password = request.POST['password'],
            birthday = request.POST['birthday'],
        )
    return redirect('/')
def login(request):
    errors = User.objects.validate(request.POST)
    if len(errors):
        for field, message in errors.iteritems():
            error(request, message, extra_tags=field)

        return redirect('/')
    if request.method == "POST":
        request.session['name'] = str(request.POST['username'])
        #everything else in this function is to check for correct password
        logged_user = request.session.get('name')
        check_pass = User.objects.get(username=logged_user)
        confirm_pass = request.POST['confirmpass']
        if check_pass.password != confirm_pass:
            return redirect('/')
        return redirect('/dashboard')

def dashboard(request):
    logged_user = request.session.get('name')
    friends_checker = User.objects.get(username=logged_user)
    context = {
        'mainuser': User.objects.get(username=logged_user),
        'users': User.objects.exclude(buddies=friends_checker).exclude(username=logged_user),
    }
    return render(request,'friends/dashboard.html', context)

def show(request, name):
    context = {
        'person': User.objects.get(name=name),
    }
    return render(request,'friends/show.html', context)

def add(request, name):
    logged_user = request.session.get('name')
    adder = User.objects.get(username=logged_user)
    added_user = User.objects.get(name=name)
    adder.buddies.add(added_user)
    #print adder.buddies.all()
    return redirect('/dashboard')

def remove(request, name):
    logged_user = request.session.get('name')
    remover = User.objects.get(username=logged_user)
    removed = User.objects.get(name=name)
    remover.buddies.remove(removed)
    return redirect('/dashboard')

def logout(request):
    del request.session['name']
    return redirect('/')