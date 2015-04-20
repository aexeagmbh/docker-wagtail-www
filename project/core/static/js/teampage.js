$(document).ready(function() {
	console.log("hi");
	$("div>li>img").click(function() {
		$("name, jobtitle, telephone, email").slideUp("fast", function() {};)
	};)

};)