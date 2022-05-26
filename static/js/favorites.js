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



// const btndelete = document.querySelector('.delete');

// function deleteReview(evt){

// }