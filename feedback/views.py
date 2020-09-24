from django.http import HttpResponse
from django.shortcuts import render
from feedback.forms import FeedbackForm
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def feedback_submit(request):
    if request.method == "GET":
        return render(request, "feedback/feedback_form.html")

    if request.method == "POST":
        # orientation = request.POST['orientation']
        # name = request.POST['name']
        # participant_type = request.POST['participant_type']
        # college = request.POST['college']
        # degree = request.POST['degree']
        # department = request.POST['department']
        # year = request.POST['year']
        # orientation_rating = request.POST['ratings']

        form = FeedbackForm(request.POST or None)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.email = request.POST['email']
            feedback.other_comments = request.POST['other_comments']
            feedback.save()

        return HttpResponse("Got response")

