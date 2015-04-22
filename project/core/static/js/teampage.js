$(document).ready(function() {

	var animateElements = function(that) {
		event.preventDefault();
	
		
		var offset = 14;
		var elements = that.parents(".employee").children(" .jobtitle, .email , .telephone");
		elements.stop();
		if (that.hasClass("isDown")) {
				var d = 0;

		that.children("img").css(
		{

			'-moz-transform': 'rotate(' + d + 'deg)',
			'-webkit-transform': 'rotate(' + d + 'deg)',
			'-o-transform': 'rotate(' + d + 'deg)',
			'-ms-transform': 'rotate(' + d + 'deg)',
			'transform': 'rotate(' + d + 'deg)'

		});
			elements = elements.map(function() {
				return $(this).animate({
					bottom: '6rem'
				}, 1000)
			})

		} else {

				var d = -90;

		that.children("img").css(
		{

			'-moz-transform': 'rotate(' + d + 'deg)',
			'-webkit-transform': 'rotate(' + d + 'deg)',
			'-o-transform': 'rotate(' + d + 'deg)',
			'-ms-transform': 'rotate(' + d + 'deg)',
			'transform': 'rotate(' + d + 'deg)'

		});
			elements = elements.map(function() {

				offset -= 2;
				return $(this).animate({


					bottom: offset + 'rem'

				}, 1000)
			});

		}

		that.toggleClass("isDown");
		return false;

	}
	$(".arrow-icon").click(function() {

		animateElements($(this));

	})



});