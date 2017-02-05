// Note: This example requires that you consent to location sharing when
      // prompted by your browser. If you see the error "The Geolocation service
      // failed.", it means you probably did not give permission for the browser to
      // locate you.

// ------Global Variables-----
var map; // The map object
var pickUp; //pick-up location
var cpos; //current location
var dest; //destination

// -----Generate Map-----
function createMap(){
  map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: 18.0179, lng: -76.8199},
    zoom: 14
  });
  getCurrent();
  addressSearch();
  //route();
}

// Returns the current location of the user
function getCurrent() {
//------Try HTML5 geolocation.------
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(function(position) {
      cpos = {
        lat: position.coords.latitude,
        lng: position.coords.longitude
      };
    // infoWindow.setPosition(pos);
    // infoWindow.setContent('Your Location.');
     pickUp =new google.maps.Marker({
      position:cpos,
      title: 'Current Location',
      draggable:true
    });
    map.setCenter(cpos);
    pickUp.setMap(map);

  }, function() {
    // handleLocationError(true, infoWindow, map.getCenter());
  });
  }
}

// ----- Address search Listener---
function addressSearch(){
  var geocoder = new google.maps.Geocoder();
  document.getElementById(/*'Your ID'*/).addEventListener('click',function(){
    geocodeAddress(geocoder,map);
  });
}

/* -----Translates an Address into coodinates
 and places pick-up marker at that location---*/
function geocodeAddress(geocoder,resultsMap){
  var address= document.getElementById('address').value;
  geocoder.geocode({'address': address},function(results,status){
    if (status === 'OK'){
      resultMap.setCenter(results[0].geometry.location);
      pickUp= {position:results[0].geometry.location,
      title:'Pick Up'
      }
    }else{
      alert('We could not locate the address you entered. Status: '+status);
    }
  });
}
