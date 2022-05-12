



function initMap(){

    const Nirvana = {
        lat: lat,
        lng: lon,
      };

    const basicMap = new google.maps.Map(document.querySelector('#map'), {
        center: Nirvana,
        zoom: 13,
      });

      const CoffeeMarker = new google.maps.Marker({
        position: Nirvana,
        title: 'Coffee',
        map: basicMap,
      });

}