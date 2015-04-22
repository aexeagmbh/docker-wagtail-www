$(document).ready(function() {

	var animateElements = function(that) {


		var icon1 = that.find('.arrow-icon-1>img');
		var icon2 = that.find('.arrow-icon-2>img');
		
		event.preventDefault();
		
		if (that.children().hasClass('telephone')) {

			var elements = that.children(" .email , .telephone");
			var offset = 9.6 + 4;
		} else {
			var elements = that.children(".email");
			elements.css("background-color", "#DDDDDD")
			var offset = 9.6 + 2;
		}
		elements.stop();
		if (that.hasClass("isDown")) {

			elements = elements.map(function() {
				return $(this).animate({
					bottom: '7.3rem'
				}, 250)
			})

			icon1.css('visibility', 'hidden');
			icon2.css('visibility', 'visible');
		} else {
			icon1.css("visibility", "visible");
			icon2.css("visibility", "hidden");
			elements = elements.map(function() {
				offset -= 2;
				return $(this).animate({
					bottom: offset + 'rem'

				}, 250) });

		}

		that.toggleClass("isDown");
		return false;

	}
	$(".employee").click(function() {
		animateElements($(this));

	})
	$(".telephone, .email ").click(function(e) {
		e.stopPropagation();
	})


});