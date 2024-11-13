from django.shortcuts import render

# Create your views here.
# views.py
from django.shortcuts import render
from .forms import ItineraryForm
from .utils import generate_itinerary

def create_itinerary(request):
    if request.method == 'POST':
        form = ItineraryForm(request.POST)
        if form.is_valid():
            destination = form.cleaned_data['destination']
            preference = form.cleaned_data['preferences']
            initial_date = form.cleaned_data['start_date']
            final_date = form.cleaned_data['end_date']

            main_itinerary, suggestions = generate_itinerary(destination, preference, initial_date, final_date)

            return render(request, 'itinerary/result.html', {'destination': destination,'main_itinerary': main_itinerary,'suggestions': suggestions})
    else:
        form = ItineraryForm()

    return render(request, 'itinerary/create_itinerary.html', {'form': form})
