'use strict';

$(document).ready(function() {

	$('select').on('change', function() {
		loadMeasurements(
			$('select[name=devices]').val(), 
			$('select[name=comparison]').val(),
			$('select[name=area]').val()
		);
	});

	loadMeasurements(
		$('select[name=devices]').val(), 
		$('select[name=comparison]').val(),
		$('select[name=area]').val()
	);
});

function loadMeasurements(device, comparison, area) {
	var url = '/measurements/averages/' + device + '/' + comparison + '/' + area;
	console.log(url);

	$.get(url, function(data) {
		var times = _.map(_.pluck(data.measurements.average, 'time'), function(time) {
			var date = new Date();
			date.setHours(time.split(':')[0]);
			date.setMinutes(time.split(':')[1]);
			date.setSeconds(time.split(':')[2]);

			return date;
		});

		var chart = c3.generate({
			padding: {
				bottom: 10
			},
			data: {
				x: 'tijd',
				columns: [
					['tijd'].concat(times),
					['mijn apparaat'].concat(_.pluck(data.measurements.single, 'average')),
					['gemiddelde'].concat(_.pluck(data.measurements.average, 'average'))
				],
			},
			axis: {
				x: {
					label: 'meet tijd',
					type: 'timeseries',
					tick: {
						format: '%H:%M:%S'
					}
				},
				y: {
					label: 'meting',
					min: 450,
					max: 550
				}
			}
		})
	});
}