$(document).ready(function(){
    $('.remove').click(function () {
        objectID = $('.remove').attr("data-object-id")
        console.log(objectID)
        del = confirm('Are you sure?');
        if (!(del)){
            window.location.href = '/whichDash'
        } else {
            window.location.href = '/deleteUser/' + objectID
        }
    });




});

