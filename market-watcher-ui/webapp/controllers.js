myApp.controller('searchController', ['$scope', '$filter', '$resource', '$http','$location', 'searchService', function($scope, $filter, $resource, $http, $location, searchService) {
	$scope.name ="search result page";

//    $http.get('assets/results.json')
//    .success(function(result){
//        $scope.realEstates = result;
//    })
//    .error(function(data, status){
//        console.log(data);
//    });

    $scope.searchApi = $resource("http://localhost:9998/realestates/", {callback: "JSON_CALLBACK"}, {get:{method:"JSONP"}});
    $scope.realEstates = $scope.searchApi.get();
    
	$scope.formattedRealEstate = function(realEstate){
		return 'price: ' + realEstate.price + ', number of bedrooms:' + realEstate.bedroomNr  + ', neighbood:' + realEstate.hood + ', posted date: ' + realEstate.postedDate;
	}
}]);

myApp.controller('forecastController', ['$scope', '$routeParams', function($scope, $routeParams) {
	$scope.name ="forecast page";
	$scope.num = $routeParams.num;
}]);

myApp.controller('notificationController', ['$scope', function($scope) {
	$scope.name ="notification page";
}]);

myApp.controller('mainController', ['$scope', '$filter', '$http', '$location', function($scope, $filter, $http, $location) {
    $scope.searchKeyword = '';
    $scope.characters = 3;
    $scope.lowercasesearchkeyword = function(){
    	return $filter('lowercase')($scope.searchKeyword);
    }
}]);