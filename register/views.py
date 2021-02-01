from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

def UserRegister(request):
    if request.method == "POST":
        fn = request.POST.get('first_name')
        ln = request.POST.get('last_name')
        e = request.POST.get('email')
        password = request.POST.get('password')

        user = User()
        user.first_name = fn
        user.last_name = ln
        user.username = e
        user.save()
        user.set_password(password)
        user.save()
        messages.success(request, "Registration successful...")
        return redirect('/')
    else:
        return render(request, 'register.html', )
