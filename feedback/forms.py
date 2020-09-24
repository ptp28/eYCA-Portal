from feedback.models import Feedback
from django import forms


class FeedbackForm(forms.ModelForm):

    class Meta:
        model = Feedback
        fields = [
            'name',
            'participant_type',
            'college',
            'degree',
            'department',
            'year',
            'orientation_rating',
        ]