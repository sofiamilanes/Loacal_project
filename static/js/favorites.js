const buttons = document.querySelectorAll('.remove');

function remove(evt){
    evt.preventDefault()
    const id = evt.target.value
    if(confirm('Are you sure you want to remove from favorites?')){
        fetch(`/${id}/unlike`)
        .then((response) => {
            document.getElementById(id).remove();
        });
    }
}

for ( const button of buttons){
    button.addEventListener('click', remove);
}



$(document).ready(function(){
        // $( "div.results-form" ).toggle( 1800 );
        $( "div.results-form" ).slideDown( 1050 );
        $( "div#account-form" ).slideDown( 1050 );
        $( "div#login-form" ).slideDown( 1050 );
        $( "div.blocktext" ).slideDown( 1050 );
        $( "div#information-form" ).slideDown( 1050 );
        $( "div#pass-form" ).slideDown( 1050 );
        $( "div#rating-form" ).slideDown( 1050 );
        $( "div#rating-form" ).slideDown( 1050 );
        $( ".rating_table" ).slideDown( 1050 );
        $( "div.all" ).toggle( 1050 );
        // $( "h2" ).toggle( 1050 );


        // $( "div.img-container img" ).delay(500).fadeIn( 400 );






        $( "div.quote" ).slideDown( 1750 );
        // $( "h1" ).slideDown( 1750 );



        $( "div.information-container" ).toggle( 1300 );
        $( "div.information-containers" ).slideDown( 1050 );

        // $( "div.information-container" ).slideDown( 1300 );





  });