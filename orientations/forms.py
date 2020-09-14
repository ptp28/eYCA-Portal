from django import forms
from orientations.models import Orientation

class OrientationForm(forms.ModelForm):
    date = forms.CharField(widget=forms.SelectDateWidget())
    time = forms.CharField(widget=forms.TimeInput())
    class Meta:
        model = Orientation
        fields = ['about', 'date', 'time', 'meeting_type', 'expected_participants', 'outreach']