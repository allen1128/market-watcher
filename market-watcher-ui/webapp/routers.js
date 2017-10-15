myApp.config(function($routeProvider){
	$routeProvider
		.when('/', {
			templateUrl: 'views/search.html',
			controller: 'searchController'
		})
		.when('/forecast:num', {
			templateUrl: 'views/forecast.html',
			controller: 'forecastController'
		})
		.when('/forecast', {
			templateUrl: 'views/forecast.html',
			controller: 'forecastController'
		})
		.when('/notification', {
			templateUrl: 'views/notification.html',
			controller: 'notificationController'
		});
});

