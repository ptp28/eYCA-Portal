from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
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
                return redirect('dashboard')
            else:
                return HttpResponse('ACCOUNT DISABLED')
                # return render(request, 'music/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return HttpResponse('NO ACCOUNT')
            # return render(request, 'music/login.html', {'error_message': 'Invalid login'})
        # return render(request, 'eyca/login.html')


def register(request):
    if request.method == 'GET':
        return render(request, 'eyca/register.html')
    if request.method == 'POST':
        fields = [
            'name',
            'email',
            'college',
            'course',
            'year',
            'dob',
            'contact_number',
            'password'
        ]

        name = request.POST['name'].split()
        college = request.POST['college']

        new_user = User()
        new_user.email = request.POST['email']
        new_user.first_name = name[0]
        new_user.last_name = name[-1]

        return HttpResponse("Registered")


def dashboard(request):
    return render(request, 'eyca/dashboard.html')


def teampage(request):
    user_list = User.objects.all()
    return render(request, 'eyca/teampage.html', {'user_list' : user_list})


def getCollegeInitials(college_name):
    college_name = college_name.upper()
    college_name = college_name.split(" ")
    college_name_initals = ""
    for word in college_name:
        college_name_initals += college_name_initals.join(word[0])
        return college_name_initals
