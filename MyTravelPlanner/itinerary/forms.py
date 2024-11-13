# forms.py
from django import forms
from django.core.exceptions import ValidationError
from datetime import date
from crispy_forms.layout import Layout,Div,Submit
from crispy_forms.helper import FormHelper

class ItineraryForm(forms.Form):
    destination = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Enter a destination'}))
    start_date = forms.DateField(label='', widget=forms.DateInput(attrs={'placeholder': 'Select start date', 'class': 'flatpickr'}),required=False)
    end_date = forms.DateField(label='', widget=forms.DateInput(attrs={'placeholder': 'Select end date', 'class': 'flatpickr'}),required=False)
    travelers = forms.IntegerField(label='', min_value=1,widget=forms.NumberInput(attrs={'min': '1', 'placeholder': 'Number of Travelers'}))
    PREFERENCES_CHOICES = [
        ('adventure', 'Adventure'),
        ('cultural', 'Cultural'),
        ('family', 'Family-friendly'),
        ('relaxation', 'Relaxation'),
        ('nature', 'Nature'),
        ('luxury', 'Luxury'),
    ]
    
    # preferences = forms.MultipleChoiceField(
    #     choices=PREFERENCES_CHOICES,
    #     widget=forms.CheckboxSelectMultiple(attrs={'placeholder': 'Enter your preferences (e.g., adventure, culture, etc.)'}),
    #     label='',
    #     required=False
    # )


    preferences = forms.ChoiceField(
        choices=PREFERENCES_CHOICES,
        label='Main Trip Preference',
        required=False
    )

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.helper = FormHelper()
        self.helper.form_class = "px-2 mt-8"
        self.helper.form_action = ""
        self.helper.layout = Layout(
            Div(
                Div('destination',css_class="lg:w-[63%]"),
                Div('travelers',css_class="lg:w-[36%]"),
                css_class="lg:flex justify-between ",
            ),
            Div(
                Div('start_date',css_class="lg:w-[49.5%]"),
                Div('end_date',css_class="lg:w-[49.5%]"),
                css_class="lg:flex justify-between mb-4",
            ),
            'preferences',
            Submit('submit','Submit',css_class="px-20 mx-auto flex min-w-[84px] max-w-[480px] cursor-pointer items-center justify-center overflow-hidden rounded-xl h-10 bg-[#F4C753] text-[#141C24] text-sm font-bold leading-normal tracking-[0.015em]")

        )
    
    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')

        # Check if the end date is before the start date
        if start_date and end_date and end_date < start_date:
            raise ValidationError('End date cannot be before start date.')

        # Check if start date is in the past
        if start_date and start_date < date.today():
            raise ValidationError('Start date cannot be in the past.')

        return cleaned_data

