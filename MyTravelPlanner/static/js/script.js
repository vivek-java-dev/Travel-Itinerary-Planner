const logoutForm = document.getElementById('logout-form') 

function showLogoutForm(){
  logoutForm.classList.remove('hidden');
}
function hideLogoutForm(){
  logoutForm.classList.add('hidden');
}


document.addEventListener('DOMContentLoaded', function () {
    flatpickr('.flatpickr', {
        dateFormat: 'Y-m-d', 
    });
});

function getDirections(lat, lng) {
    if (lat === null || lng === null){
      alert("Coordinates not available for this location.");
      return;
    }
    const googleMapsUrl = `https://www.google.com/maps/dir/?api=1&destination=${lat},${lng}`;
    window.open(googleMapsUrl, "_blank");
  }
  

// function initialize() {
//     var input = document.getElementById('id_destination');
//     var autocomplete = new google.maps.places.Autocomplete(input);
// }
// google.maps.event.addDomListener(window, 'load', initialize);