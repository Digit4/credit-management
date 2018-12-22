function makeid(n) {
	var text = "";
	var possible = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";

	for (var i = 0; i < n; i++)
		text += possible.charAt(Math.floor(Math.random() * possible.length));

	return text;
}

function saved() {
	alert("Your changes have been saved.\n Please go to transfer history to see your transaction.")
}


jQuery(document).ready(function ($) {
	console.log("Hello World!")
	var rand = makeid(10)
	$('input[name=link]').val(rand)
	//alert($("input[name=link]").val());
	//console.log("value has been assigned to link:" + rand)
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
		if (amt < 0) {
			$("#amt-id").after('<span class="error">Amont cannot be negative.</span>');
            e.preventDefault();
		}
		if (amt > chk) {
			("#amt-id").after("<span class=\"error\">This user doesn't have enough credits</span>");
			e.preventDefault();
		}
		if (selected_radios == undefined) {
			$("#amt-id").after('<span class="error">Please select a user to transfer funds to.</span>');
			e.preventDefault();
		}
	})
$
	$("#create-form").submit(function (e) {
		
		var query_string = $(this).serialize()
		// alert(makeid(10))
		//e.preventDefault();
	})
})


	