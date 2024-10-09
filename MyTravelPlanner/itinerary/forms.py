# forms.py
from django import forms

class ItineraryForm(forms.Form):
    destination = forms.CharField(label='Destination', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Enter a destination'}))
    start_date = forms.DateField(label='Start Date', widget=forms.SelectDateWidget())
    end_date = forms.DateField(label='End Date', widget=forms.SelectDateWidget())
    travelers = forms.IntegerField(label='Number of Travelers', min_value=1)
    preferences = forms.CharField(
        label='Trip Preferences', 
        widget=forms.Textarea(attrs={'placeholder': 'Enter your preferences (e.g., adventure, culture, etc.)'}),
        required=False
    )
