from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash


def home_page(request):
    return render(request, 'eyca/index.html')


def login_user(request):
    if request.method == 'GET':
        return render(request, 'eyca/login.html')

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        print(user)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('dashboard')
            else:
                return HttpResponse('ACCOUNT DISABLED')
        else:
            return HttpResponse('NO ACCOUNT')


@login_required
def activate_account(request):
    if request.method == "POST":
        new_password = request.POST['password']

        print(new_password)
        request.user.set_password(new_password)
        request.user.is_active = True
        request.user.save()
        update_session_auth_hash(request, request.user)
        return redirect('dashboard')

@login_required()
def dashboard(request):
    # return render(request, 'eyca/dashboard.html')
    return render(request, 'eyca/dashboard_under_construction.html', context={'user': request.user})


def teampage(request):
    user_list = User.objects.all()
    return render(request, 'eyca/teampage.html', {'user_list' : user_list})


def logout_user(request):
    logout(request)
    return redirect('home_page')

