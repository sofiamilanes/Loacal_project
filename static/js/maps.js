



function initMap(){

    const Nirvana = {
        lat: lat,
        lng: lon,
      };

    const basicMap = new google.maps.Map(document.querySelector('#map'), {
        center: Nirvana,
        zoom: 14,
      });

      const PlaceMarker = new google.maps.Marker({
        position: Nirvana,
        title: 'Coffee',
        map: basicMap,
        icon: {
            url: "http://maps.google.com/mapfiles/ms/icons/pink-dot.png"
          }
      });

}