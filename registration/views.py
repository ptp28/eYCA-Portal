from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from registration.models import Registration
from django.contrib.auth.models import User
from django.utils import timezone


@csrf_exempt
def register(request):
    if request.method == 'GET':
        return render(request, 'registration/register.html')
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        college = request.POST['college']
        course = request.POST['course']
        department = request.POST['department']
        year = request.POST['year']
        dob = request.POST['dob']
        contact_number = request.POST['contact_number']
        profile_pic = request.FILES['profile_pic']
        id_card = request.FILES['id_card']

        username = generate_username(college, name)

        new_user_registration = Registration()
        new_user_registration.name = name
        new_user_registration.email = email
        new_user_registration.username = username
        new_user_registration.college = college
        new_user_registration.course = course
        new_user_registration.department = department
        new_user_registration.year = year
        new_user_registration.dob = dob
        new_user_registration.phone_number = contact_number
        new_user_registration.profile_pic = profile_pic
        new_user_registration.id_card_pic = id_card
        new_user_registration.save()

        return render(request, 'registration/registration_submitted.html')


def generate_username(college_name, name):
    college_name = college_name.upper()
    college_name = college_name.strip()
    college_name = college_name.split(" ")
    college_name_initials = ""
    for word in college_name:
        college_name_initials += college_name_initials.join(word[0])

    name = name.upper()
    name = name.strip()
    name = name.split(" ")
    name_initials = ""
    for word in name:
        name_initials += name_initials.join(word[0])

    user_count = User.objects.all().count()

    username = ""
    username = college_name_initials
    username += str(timezone.now().year)
    username += name_initials
    username += str(user_count)

    return username
