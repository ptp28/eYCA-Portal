from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User


def home_page(request):
    return render(request, 'eyca/index.html')


def login_user(request):
    if request.method == 'GET':
        return render(request, 'eyca/login.html')

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponse('LOGIN SUCCESSFUL')
            else:
                return HttpResponse('ACCOUNT DISABLED')
                # return render(request, 'music/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return HttpResponse('NO ACCOUNT')
            # return render(request, 'music/login.html', {'error_message': 'Invalid login'})
        # return render(request, 'eyca/login.html')


def register(request):
    return render(request, 'eyca/register.html')


def dashboard(request):
    return render(request, 'eyca/dashboard.html')


def teampage(request):
    user_list = User.objects.all()
    return render(request, 'eyca/teampage.html', {'user_list' : user_list})
