$(document).ready(function() {

	var animateElements = function(that) {

		var icon1 = that.find('.arrow-icon>img');

		event.preventDefault();
		var elements= that.find('.contact-container');
		var telephone= elements.children('.telephone');
		 if (!(telephone.hasClass('telephone'))) {
			var email=elements.children('.email');
			email.css("background-color", "#DDDDDD");
		 	}
		
		elements.stop();
		if (that.hasClass("isDown")) {

			elements = elements.map(function() {
				return $(this).animate({
					bottom: "-4rem",
				}, 250)
			})

			icon1.css({
				'-ms-transform': 'rotate(0deg)',
				'-webkit-transform': 'rotate(0deg)',
				'transform': 'rotate(0deg)'
			});
		} else {
		icon1.css({
				'-ms-transform': 'rotate(-90deg)',
				'-webkit-transform': 'rotate(-90deg)',
				'transform': 'rotate(-90deg)'
			});

			elements = elements.map(function() {
				return $(this).animate({
					bottom: '0rem',

				}, 250)
			});

		}

		that.toggleClass("isDown");
		

	}
	$(".employee").click(function() {
		animateElements($(this));

	})	
	$(".telephone, .email  .img").click(function(e) {
		e.stopPropagation();
	})


});