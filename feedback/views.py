from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def feedback_submit(request):
    if request.method == "GET":
        return render(request, "feedback/feedback_form.html")

    if request.method == "POST":
        orientation = request.POST['orientation']
        name = request.POST['name']
        participant_type = request.POST['participant_type']
        course = request.POST['course']
        specialisation = request.POST['specialisation']
        email = request.POST['email']
        ratings = request.POST['ratings']
        comments = request.POST['comments']
        return HttpResponse("Got response")

