$(document).ready(function() {

	var contactContainer = $('.contact-container');
	contactContainer.map(function() {

		return ($(this).children(".email").outerHeight()>40)? $(this).addClass("has-break"): false;
	});


	var animateElements = function(that) {

		event.preventDefault();
		var icon1 = that.find('.arrow-icon>img'),
		elements = that.find('.contact-container'),
		telephone = elements.children('.telephone');

		if (!(telephone.hasClass('telephone'))) {
			var email = elements.children('.email');
			email.css("background-color", "#DDDDDD");
		}
		var animateTo= elements.hasClass('.has-break') ? '-5rem' : '-8rem';

		elements.stop();
		if (that.hasClass("isDown")) {

			elements = elements.map(function() {
				return $(this).animate({
					bottom: animateTo ,
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
	contactContainer.click(function(e) {
		e.stopPropagation();
	})


});