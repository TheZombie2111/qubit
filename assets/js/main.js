"use strict";

$(document).ready(function(){
		$.ajax({
		method: 'POST',
		url: '/request',
	}).done(function(response){
		for(var i in response){
			$('.result').append(`
					<div class='result__line'>
						<div class='result__column'>${response[i]['Imei']}</div>
						<div class='result__column'>${response[i]['CurrentDateTime']}</div>
						<div class='result__column'>${response[i]['GPSDateTime']}</div>
						<div class='result__column'>${response[i]['Datatype']}</div>
						<div class='result__column'>${response[i]['Address']}</div>
						<div class='result__column'>${response[i]['Distance']}</div>
					</div>
				`
			);
		}
	})
});