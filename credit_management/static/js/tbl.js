jQuery(document).ready(function ($) {
	/* $(".clickable-row").click(function () {
		window.location = $(this).data("href");
	});
	$(".clickable-row").on('mouseenter', function () {
		$(this).toggleClass('hovering-over')
	})
	$(".clickable-row").on("mouseleave", function() {
        $(this).toggleClass("hovering-over");
	}); */
	$("tr").on('click-row.bs.table', function (e, row, $element) {
		window.location = $element.data('href');
	});
});

