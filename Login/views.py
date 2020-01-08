from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth


# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        pass1 = 'chiefgeek'

        if username == 'admin':
            if pass1 == password:
                auth.login(request, user)
                return redirect('admin_page')

        if user is not None:
            auth.login(request, user)
            return redirect('login_buy')

        else:
            messages.info(request, 'Check your details..')
            return redirect('login')
    else:
        return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:

            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email exist')
                return redirect('register')
            elif len(password1) < 8:
                messages.info(request, 'I need security!')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email,
                                                first_name=first_name,
                                                last_name=last_name)
                user.save()
                print('User Created')
                return redirect('login')

        else:
            messages.info(request, 'Password not match')
            return redirect('register')
        return redirect('/')

    else:
        return render(request, "register.html")
