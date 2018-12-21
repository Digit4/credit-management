
jQuery(document).ready(function ($) {
	console.log("Hello World!")

	function alertUserHome(toHome, message) {
		console.log(toHome);
		alert(message);
		window.location.href(toHome);
		return false;
	}

	$("#my-form").submit(function(e) {
		var chk = parseInt($('#credit-id').text());
		var amt = parseInt($('#amt-id').val());
		var selected_radios = $("input[name='reciever_email']:checked").val()
		$('.error').remove()
		console.log("The user has:" + chk + "\nAnd the user wants to transfer:" + amt);
		console.log("user selected: " + selected_radios)
		if (amt > chk) {
			$("#amt-id").after("<span class=\"error\">This user doesn't have enough credits</span>");
			e.preventDefault();
		}
		if (selected_radios == undefined) {
			$("#amt-id").after('<span class="error">Please select a user to transfer funds to.</span>');
			e.preventDefault();
		}
	})
})


	