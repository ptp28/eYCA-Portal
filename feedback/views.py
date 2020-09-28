from django.http import HttpResponse
from django.shortcuts import render
from feedback.forms import FeedbackForm
from datetime import date, timedelta
from django.views.decorators.csrf import csrf_exempt

from orientations.models import Orientation


@csrf_exempt
def orientations_list(request):
    if request.method == "GET":
        date_today = date.today()
        date_yesterday = date.today() - timedelta(days=1)
        orientations_today = Orientation.objects.filter(date=date_today)
        orientations_yesterday = Orientation.objects.filter(date=date_yesterday)
        context = {
            'date_today': date_today,
            'orientations_today': orientations_today,
            'date_yesterday': date_yesterday,
            'orientations_yesterday': orientations_yesterday
        }
        return render(request, "feedback/orientation_list.html", context)


@csrf_exempt
def feedback_submit(request, orientation_id):
    if request.method == "GET":
        context = {'orientation_id': orientation_id}
        return render(request, "feedback/feedback_form.html", context)

    if request.method == "POST":
        form = FeedbackForm(request.POST or None)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.email = request.POST['email']
            feedback.other_comments = request.POST['other_comments']
            feedback.save()

        return HttpResponse("Got response")

