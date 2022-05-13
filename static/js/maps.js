



function initMap(){

    const Place = {
        lat: lat,
        lng: lon,
      };


    const basicMap = new google.maps.Map(document.querySelector('#map'), {
        center: Place,
        zoom: 14,
      });

      const PlaceMarker = new google.maps.Marker({
        position: Place,
        title: 'Coffee',
        map: basicMap,
        icon: {
            url: "http://maps.google.com/mapfiles/ms/icons/pink-dot.png"
          }
      });

      // current location 
    document.querySelector('#current-location').addEventListener('click', () =>{
        const current = navigator.geolocation.getCurrentPosition((position)=>{
            window.userLocation = {
                lat: position.coords.latitude,
                lng: position.coords.longitude
            };
            console.log(userLocation)

            basicMap.setCenter(userLocation);
            basicMap.setZoom(13);
        })

        document.querySelector('#get-directions').addEventListener('click',() =>{



            const directionsService = new google.maps.DirectionsService();


            const directionsRenderer = new google.maps.DirectionsRenderer();
            directionsRenderer.setMap(basicMap);

            const Route= {
                origin: window.userLocation,
                // origin:{
                //     lat: 37.3298493,
                //     lng: -121.8869697,
                // },

                destination: Place,

                travelMode:'WALKING'
            };
            directionsService.route(Route,(response, status)=>{
                if(status === 'OK'){
                    directionsRenderer.setDirections(response)
                }else{
                    alert(`DIRECTIONS ${status}`)
                }
            });
          });
      });
}