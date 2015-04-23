$(document).ready(function() {

	var animateElements = function(that) {


		var icon1 = that.find('.arrow-icon>img');

		event.preventDefault();

		if (that.children().hasClass('telephone')) {

			var elements = that.children(" .email , .telephone");
			var offset = 10.7 + 4;
		} else {
			var elements = that.children(".email");
			elements.css("background-color", "#DDDDDD")
			var offset = 10.7 + 2;
		}
		elements.stop();
		if (that.hasClass("isDown")) {

			elements = elements.map(function() {
				return $(this).animate({
					bottom: '7rem'
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
				offset -= 2;
				return $(this).animate({
					bottom: offset + 'rem'

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