import requests
from django.conf import settings
from datetime import datetime

def get_gomaps_places(destination, preference):
    api_key = settings.GOMAPS_API_KEY
    endpoint = "https://maps.gomaps.pro/maps/api/place/textsearch/json"
    query = f"{preference} in {destination}"

    params = {
        'query': query,
        'key': api_key
    }

    response = requests.get(endpoint, params=params)

    if response.status_code == 200:
        results = response.json().get('results', [])
        places = [
            {
                'name': place['name'],
                'address': place.get('formatted_address', 'No address provided'),
                'rating': place.get('rating', 'No rating available'),
                "lat": place.get("geometry", {}).get("location", {}).get("lat"),
                "lng": place.get("geometry", {}).get("location", {}).get("lng")
                
            }
            for place in results
        ]
        return places
    else:
        return []


def generate_itinerary(destination, preference, initial_date, final_date):
    number_of_days = get_number_of_days(initial_date, final_date)
    places = get_gomaps_places(destination, preference)

    main_itinerary = []
    suggestions = []

    # Generate the main itinerary
    for day in range(number_of_days):

        if day < len(places):
            place = places[day]

            main_itinerary.append({
                'day': f"Day {day + 1}",
                'name': place['name'],
                'address': place['address'],
                'rating': place['rating'],
                "lat": place["lat"],
                "lng": place["lng"]
    
            })
        else:
            # Placeholder if there are fewer places than days
            main_itinerary.append({
                'day': f"Day {day + 1}",
                'name': "Free Day / Explore on Your Own",
                'address': "No specific place found.",
                'rating': "N/A"
            })

    # Generate suggestions (3 additional places)
    for place in places[number_of_days:number_of_days + 3]:
        suggestions.append({
            'name': place['name'],
            'address': place['address'],
            'rating': place['rating'],
            "lat": place["lat"],
            "lng": place["lng"]
    

        })


    return main_itinerary, suggestions




def get_number_of_days(initial_date, final_date):
   
    number_of_days = (final_date - initial_date).days + 1  # Including the final day
    return max(1, number_of_days)  # Ensure at least 1 day