from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render


def schedule_orientation(request):
    if request.method == "GET":
        return render(request, "orientations/orientation_add_form.html")

    if request.method == "POST":
        about = request.POST['about']
        date = request.POST['date']
        time_from = request.POST['time_from']
        time_till = request.POST['time_till']
        meeting_type = request.POST['meeting_type']
        num_participants = request.POST['num_participants']
        outreach = request.POST['outreach']
        return HttpResponse("Got response")

