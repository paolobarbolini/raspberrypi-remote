$(".onoffswitch-checkbox").click(function() {
	$.ajax({
		url: "/switch/" + $(this).data("id"),
		method: "POST"
	});
});
