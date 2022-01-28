$(document).ready(function(){
$(".true_btn").click(function(){
    $.ajax({
        url: '',
        type:'get',
        data:{
            true_button: $(this).text()
        },
        success: function(response){
            $(".true_btn").text(response.seconds)
        }
    });
});



//$(".false_btn")



});