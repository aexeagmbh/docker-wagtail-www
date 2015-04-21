$(document).ready(function() {

	$(".arrow-icon").click(function() {
		var deg=-90;

		$(this).children("img").animate( {

                   transform: 'rotate('+deg+'deg)'
		},1000);

		$(this).parents(".employee").children(".name , .jobtitle, .telephone , .email").animate({
			display:'initial',
			
			top:'-11rem'

		},1000);
	});
	
});