"use strict";

$(document).ready(function(){
	var results = $(document).find('.result');
	if (window.location.pathname == '/frontend'){
		$.ajax({
			method: 'POST',
			url: '/request',
		}).done(function(response){
			for(var i in response){
				$(results[0]).append(`
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
				if (response[i]['Datatype'] == 1){
					var prev = response[i]['Distance'];
					var prevDate = new Date(response[i]['CurrentDateTime']);
				}
				if (response[i]['Datatype'] == 2){
					var hours = (new Date(response[i]['CurrentDateTime']).getHours() - prevDate.getHours());
					var minutes = (new Date(response[i]['CurrentDateTime']).getMinutes() - prevDate.getMinutes());
					minutes < 0 ? minutes = -minutes : false;
					String(minutes).length < 2 ? minutes = '0' + String(minutes) : false;
					var time = hours + ':' + minutes;
					$(results[1]).append(`
						<div class='result__line'>
							<div class='result__column'>${time}</div>
							<div class='result__column'>${response[i]['Datatype']}</div>
							<div class='result__column'>${response[i]['Address']}</div>
							<div class='result__column'>${response[i]['Distance'] - prev}</div>
						</div>
						`
					);
				};
			}
		});
	}

	let switchers = $(document).find('.switcher').find('.switcher__item');
	let tabs = $(document).find('.tab');

	switchers.each(function(index){
		$(this).click(function(){
			switchers.removeClass('active');
			tabs.removeClass('active');
			$(this).addClass('active');
			$(tabs[index]).addClass('active');
		});
	});
});