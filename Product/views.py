from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth.models import User, auth
from .models import Racket
from .forms import ImageForm
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.db import connection
from django.core.mail import send_mail


# Create your views here.

def buy(request):
    dest = Racket.objects.all()
    return render(request, 'buypage.html', {'obj': dest})


def stuff(request):
    current_user = request.user
    dest = Racket.objects.filter(username=current_user)
    return render(request, 'your_stuff.html', {'obj': dest})


def admin_page(request):
    dest = Racket.objects.all()
    return render(request, 'admin_page.html', {'obj': dest})


def login_buy(request):
    dest = Racket.objects.all()
    return render(request, 'login_buy.html', {'obj': dest})


def sell(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            username = request.user.username

            if username == 'admin':
                messages.info(request, 'Uploaded successfully!!')
                return redirect('admin_page')
            else:
                messages.info(request, 'Uploaded successfully!!')
                return redirect('stuff')
    else:
        form = ImageForm()
    return render(request, 'sellpage.html', {'form': form})


def delete_product(request):
    if request.GET.get('id'):
        i = request.GET['id']
        with connection.cursor() as cursor:
            cursor.execute('delete from product_racket where id=%s', [i])

    username = request.user.username
    if username == 'admin':
        messages.info(request, 'Deleted successfully!!')
        return redirect('admin_page')
    else:
        messages.info(request, 'Deleted successfully!!')
        return redirect('buy')


def update_product(request):
    if request.method == 'POST':
        name_seller = request.POST['name_seller']
        print(name_seller)
        Racket.objects.filter(id=29).update(name_seller='name_seller')

        return render(request, 'your_stuff.html')

    else:
        return render(request, 'update_product.html')


def thanks(request):
    z = request.user.email
    a = request.user.first_name
    b = request.user.last_name

    if request.GET.get('email'):
        x = request.GET['email']

        send_mail(
            'Product Purchase Notification',
            'This is the admin of the website. ' + a + ' ' + b + ' wants to buy the product.' + ' Contact the seller on this email id: '
            + z + '\nThank you',
            'jackphoneix1234@gmail.com',
            [x],
            fail_silently=False)

    return render(request, 'thanks.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
