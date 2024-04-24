from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate
from django.contrib import messages
from django.contrib.auth import login as auth_login

User = get_user_model()


def sing_up(request):
    if request.method == 'POST':
        username = request.POST['username']
        nick = request.POST['nick']
        avatar = request.FILES['avatar']
        bio = request.POST['bio']
        password_1 = request.POST['password_1']
        password_2 = request.POST['password_2']
        if password_1 == password_2:
            try:
                user = User.objects.create(username=username, nick=nick, avatar=avatar, bio=bio)
                user.set_password(password_1)
                user.save()
                user = authenticate(username=username, password=password_1)
                auth_login(request, user)
                return redirect('index')
            except:
                messages.error(request, 'неправ ты короче')
        else:
            messages.error(request, 'пароли не совпадают')
    return render(request, 'users/registration.html')


def login(request):
    if request.method == 'POST':
        try:
            username = request.POST['username']
            password = request.POST['password']
            user = User.objects.get(username=username)
            auth_user = authenticate(username=username, password=password)
            auth_login(request, auth_user)
            return redirect('index')
        except:
            messages.error(request, 'неверный логин или пароль')
    return render(request, 'users/login.html')




