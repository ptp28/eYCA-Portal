from django import forms
from orientations.models import Orientation


class OrientationForm(forms.ModelForm):

    class Meta:
        model = Orientation
        fields = [
            'about',
            'date',
            'time_from',
            'time_till',
            'meeting_type',
            'expected_participants',
            'outreach'
        ]