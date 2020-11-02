from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from .forms import OrientationForm


@login_required
def schedule_orientation(request):
    if request.method == "GET":
        return render(request, "orientations/orientation_add_form.html")

    if request.method == "POST":
        form = OrientationForm(request.POST or None)
        if form.is_valid():
            orientation = form.save(commit=False)
            orientation.status = "Scheduled"
            orientation.save()
            return HttpResponse("Got response")
        else:
            return HttpResponse("Got no response")


@login_required
def orientation_report(request):
    pass
