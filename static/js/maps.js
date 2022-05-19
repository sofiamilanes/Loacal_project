



// function initMap() {

//     const Place = {
//         lat: lat,
//         lng: lon,
//     };



//     const basicMap = new google.maps.Map(document.querySelector('#map'), {
//         center: Place,
//         zoom: 14,
//     });


//     const PlaceMarker = new google.maps.Marker({
//         position: Place,
//         map: basicMap,
//         icon: {
//             url: "http://maps.google.com/mapfiles/ms/icons/pink-dot.png"
//         }
//     });


//     const current = navigator.geolocation.getCurrentPosition((position)=>{
//         window.userLocation = {
//             lat: position.coords.latitude,
//             lng: position.coords.longitude
//         };
//         console.log(userLocation)

//     })
//     // const directionsRenderer = new google.maps.DirectionsRenderer();


//     document.querySelector('#directions').addEventListener('click',directions)

//     function directions(evt){
//         // const method = evt.target.value
//         const selectedMode = document.getElementById("mode").value;
//         const button = document.querySelector('#dir').innerHTML = '<button> button </button>'
//         const directionsService = new google.maps.DirectionsService();


//         const directionsRenderer = new google.maps.DirectionsRenderer();
//         directionsRenderer.setMap(basicMap);
//         directionsRenderer.setPanel(document.getElementById("sidebar")); //!
//         // const directions = directionsRenderer.getDirections();
//         // console.log(directionsRenderer.getDirections())

//         const Route= {
//             origin: window.userLocation,

//             destination: Place,

//             travelMode:selectedMode,

//         };
//         directionsService.route(Route,(response, status)=>{
//             if(status === 'OK'){
//                 directionsRenderer.setDirections(response)
//             }else{
//                 alert(`Directions request unsuccessful due to ${status}`)
//             }
//         });
        
//     }
//     // document.querySelector('#dir').addEventListener('click', (evt) => {
//     //     console.log('hello')
//     // })
// }








function initMap() {
    const directionsRenderer = new google.maps.DirectionsRenderer();

    const directionsService = new google.maps.DirectionsService();

    const Place = {
        lat: lat,
        lng: lon,
    };
    const basicMap = new google.maps.Map(document.querySelector('#map'), {
        center: Place,
        zoom: 14,
    });
    directionsRenderer.setMap(basicMap);

    const PlaceMarker = new google.maps.Marker({
        position: Place,
        map: basicMap,
        icon: {
            url: "http://maps.google.com/mapfiles/ms/icons/pink-dot.png"
        }
    });


    const current = navigator.geolocation.getCurrentPosition((position)=>{
        window.userLocation = {
            lat: position.coords.latitude,
            lng: position.coords.longitude
        };
        console.log(userLocation)

    })


    document.querySelector('#directions').addEventListener('click',directions)

    function directions(evt){
        const selectedMode = document.getElementById("mode").value;
        directionsRenderer.setPanel(document.getElementById("sidebar")); //!


        const Route= {
            origin: window.userLocation,

            destination: Place,

            travelMode:selectedMode,

        };
        directionsService.route(Route,(response, status)=>{
            if(status === 'OK'){
                directionsRenderer.setDirections(response)
            }else{
                alert(`Directions request unsuccessful due to ${status}`)
            }
        });
        
    }
    // document.querySelector('#dir').addEventListener('click', (evt) => {
    //     console.log('hello')
    // })
}