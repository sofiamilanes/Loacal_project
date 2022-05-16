const buttons = document.querySelectorAll('.remove');

function remove(evt){
    evt.preventDefault()
    const id = evt.target.value
    if(confirm('Are you sure you want to remove this?')){
        fetch(`/${id}/unlike`)
        .then((response) => {
            document.getElementById(id).remove();
        });
    }
}

for ( const button of buttons){
    button.addEventListener('click', remove);
}

// const addReview = document.querySelector('.addReview');

// function addReview(evt){
//     evt.preventDefault()
// }