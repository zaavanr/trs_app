// Note: This example requires that you consent to location sharing when
      // prompted by your browser. If you see the error "The Geolocation service
      // failed.", it means you probably did not give permission for the browser to
      // locate you.

// ------Global Variables-----
var map; // The map object
var pickUp; //pick-up location Marker
var cpos; //current (position) location of device
var dest; //destination Marker
var destLoc;//destination location
var pickUpLoc; //Pick up location
var pos;
var coords;
var geocoder;
// -----Generate Map-----
function createMap(){
  map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: 18.0179, lng: -76.8199},
    zoom: 14
  });
  geocoder = new google.maps.Geocoder();
  getCurrent();
  setPickUp();
  // setDestination();
  // drawRoute(pickUpLoc,destLoc);
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
    pickUp =new google.maps.Marker({
      position:cpos,
      title: 'Current Location',
      draggable:true
    });
    pickUpLoc=cpos;
    map.setCenter(cpos);
    pickUp.setMap(map);
    console.log("current pos; lat:"+cpos.lat+" lng:"+cpos.lng);
    console.log("Pickup if set to current: "+pickUpLoc.lat+","+pickUpLoc.lng);
    //geocodeAddress(map)
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

function setPickUp(){
  ///document.getElementById(/*'Your ID'*/).addEventListener('click',function(){
    var address='656 Hope Rd Kingston';
    geocoder.geocode({'address': address},function(results,status){
      if (status === 'OK'){
        pickUpLoc = results[0].geometry.location;
      }else{('We could not locate the address you entered. Status: '+status);}
  //});
  console.log("Pick up Loc if search "+pickUpLoc);
  // pickUp =new google.maps.Marker({
  //   position:pickUpLoc,
  //   title: 'Pick up',
  //   draggable:true,
  //   center: pickUpLoc
  // });
  pickUp.setPosition(pickUpLoc);
  pickUp.setMap(map);
  pickUp.setTitle("Pick up");
  map.setCenter(pickUpLoc);
});
}
function setDestination(){
  ///document.getElementById(/*'Your ID'*/).addEventListener('click',function(){
    var address='121 Old Hope Road, Kingston';
    geocoder.geocode({'address': address},function(results,status){
      if (status === 'OK'){
        destLoc = results[0].geometry.location;
      }else{('We could not locate the address you entered. Status: '+status);}
  //});
  console.log("Destination "+destLoc);
  dest =new google.maps.Marker({
    position:destLoc,
    title: 'Destination',
    draggable:false
  });
  dest.setMap(map);
  map.setCenter(destLoc);
});
// drawRoute(pickUpLoc,destLoc);
}

// ----- Address search Listener---
// function addressSearch(){
//   //var geocoder = new google.maps.Geocoder();
//   ///document.getElementById(/*'Your ID'*/).addEventListener('click',function(){
//     var address='656 Hope Rd Kingston';
//     geocodeAddress(address);
//   //});
// }

/* -----Translates an Address into coodinates
 and places pick-up marker at that location---
 @param: geocoder:Geocoder object
        map: map object*/

// function geocodeAddress(address){
//   var geocoder = new google.maps.Geocoder();
//   //var address= '656 Hope Rd Kingston';//document.getElementById('address').value;
//   geocoder.geocode({'address': address},function(results,status){
//     if (status === 'OK'){
//       var coords= results[0].geometry.location;
//       console.log ("coords "+coords);
//       return coords;
//       // map.setCenter(results[0].geometry.location);
//       // pickUp =new google.maps.Marker({
//       // position:results[0].geometry.location,
//       // title: 'Pick up location',
//       // draggable:true
//       // });
//       // pos.setMap(null);
//       // pickUp.setMap(map);
//       // console.log("pickUp "+pickUp.position);
//     }else{
//       alert('We could not locate the address you entered. Status: '+status);
//     }
//   });
// }

/*-----Draw route between two points-----
@param: pickUp: pick up coordinates
        dest: destination coordinates*/
function drawRoute(pickUpLoc,destLoc){
  var directionsService = new google.maps.DirectionsService;
  var directionsDisplay = new google.maps.DirectionsRenderer;
  directionsDisplay.setMap(map);
  //document.getElementById(/*Search/Request*/).addEventListener('click',function(){
    directionsService.route({
    origin: '656 Hope Rd Kingston',//document.getElementById(/*pickUp*/).value,
    destination: '121 Old Hope Road, Kingston',//document.getElementById(/*dest*/).value,
    //waypoints: ['656 Hope Rd Kingston'],
    travelMode: 'DRIVING'
    },function(response,status){
        if(status=='OK'){
          directionsDisplay.setDirections(response);
          //destLoc.setMap(null);
        }else{console.log("directions failed: "+status);}
    });console.log("Route");
  //});
}
