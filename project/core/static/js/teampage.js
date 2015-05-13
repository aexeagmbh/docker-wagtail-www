$(document).ready(function() {
	'use strict';
	(function($) {
		
		var $contactContainers = $('.employees').find('.contact-container');

		console.log($contactContainers);
		$.each($contactContainers, function() {
			var $this = $(this).children(".email");
			var lineHeight = $this.css('line-height');
			console.log(lineHeight);
			lineHeight = lineHeight.substring(0,5);
			lineHeight= parseFloat(lineHeight);
			$this.height() > lineHeight ? $(this).addClass("has-break") : false;
		});
		var animateElements = function(self) {

			var icon = self.find('.arrow-icon>img'),
				elements = self.find('.contact-container'),
				telephone = elements.children('.telephone');

			if (!(telephone.hasClass('telephone'))) {
				var email = elements.children('.email');
				//
				email.css("background-color", "#DDDDDD");
			}
			var animateTo = elements.hasClass('.has-break') ? '-5rem' : '-8rem';

			elements.stop();
			if (self.hasClass("isDown")) {
				$.each(elements, function() {
					return $(this).animate({
						bottom: animateTo,
					}, 250);
				});
				icon.css({
					'-ms-transform': 'rotate(0deg)',
					'-webkit-transform': 'rotate(0deg)',
					'transform': 'rotate(0deg)'
				});
			} 
			else {
				icon.css({
					'-ms-transform': 'rotate(-90deg)',
					'-webkit-transform': 'rotate(-90deg)',
					'transform': 'rotate(-90deg)'
				});
				$.each(elements, function() {
					return $(this).animate({
						bottom: 0,
					}, 250);
				});

			}
			self.toggleClass("isDown");


		};
		$(".employee").click(function() {
			animateElements($(this));

		});
		$contactContainers.click(function(e) {
			e.stopPropagation();
		});

	})(jQuery);
});