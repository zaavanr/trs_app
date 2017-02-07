// Note: This example requires that you consent to location sharing when
      // prompted by your browser. If you see the error "The Geolocation service
      // failed.", it means you probably did not give permission for the browser to
      // locate you.

// ------Global Variables-----
var map; // The map object
var pickUp; //pick-up location
var cpos; //current (position) location of device
var dest ={lat:18.017213,
            lng: -76.758697}; //destination
var cloc; //Client location
var pos;

// -----Generate Map-----
function createMap(){
  map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: 18.0179, lng: -76.8199},
    zoom: 14
  });
  getCurrent();
}

// --Returns the current location of the user--
function getCurrent() {
//------HTML5 geolocation.------
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(function(position) {
      cpos = {
        lat: position.coords.latitude,
        lng: position.coords.longitude
      };
    pos =new google.maps.Marker({
      position:cpos,
      title: 'Current Location',
      draggable:true
    });
    map.setCenter(cpos);
    pos.setMap(map);
    console.log("current pos; lat:"+cpos.lat+" lng:"+cpos.lng)
    geocodeAddress(map)
    // $.ajax('/save-coord', {
    //   data: {
    //     x:  '12',
    //     y: '123'
    //   },
    //   method: 'POST'
    // }).then(function(response) {
    //    console.log(response);
    //   //  var coords = JSON.parse('{x: 12, y:13}');
    //   var coords = response;
    //    console.log(coords.xcoord);
    // });
    }, function() {
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
 and places pick-up marker at that location---
 @param: geocoder:Geocoder object
        map: map object*/
function geocodeAddress(map){
  var geocoder = new google.maps.Geocoder();
  var address= '656 Hope Rd Kingston';//document.getElementById('address').value;
  geocoder.geocode({'address': address},function(results,status){
    if (status === 'OK'){
      map.setCenter(results[0].geometry.location);
      pickUp =new google.maps.Marker({
      position:results[0].geometry.location,
      title: 'Current',
      draggable:true
      });
      pos.setMap(null);
      pickUp.setMap(map);
      console.log("pickUp "+pickUp.position);
    }else{
      alert('We could not locate the address you entered. Status: '+status);
    }
  });
}

/*-----Draw route between two points-----
@param: pickUp: pick up coordinates
        dest: destination coordinates*/
function drawRoute(pickUp,dest){
  var directionsService = new google.maps.DirectionsService;
  var directionsDisplay = new gogle.maps.DirectionsRenderer;
  directionsDisplay.setMap(map);
  document.getElementById(/*Search/Request*/).addEventListener('click',function(){
    directionsService.route({
    origin: document.getElementById(/*pickUp*/).value,
    destination: document.getElementById(/*dest*/).value,
    waypoints: cloc,
    travelMode: 'DRIVING'
    },function(response,status){
        if(status=='OK'){
          directionsDisplay.setDirections(response);
        }else{console.log("directions failed: "+status);}
    });
  });
}
