myApp.controller('searchController', ['$scope', '$filter', '$resource', '$http','$location', 'searchService', 'Pagination', function($scope, $filter, $resource, $http, $location, searchService, Pagination) {
    var PAGE_SIZE = 10;
	$scope.name ="search result page";
    $scope.pagination = Pagination.getNew(PAGE_SIZE);

//    $http.get('assets/results.json')
//    .success(function(result){
//        $scope.realEstates = result;
//    })
//    .error(function(data, status){
//        console.log(data);
//    });
//
//    $scope.searchApi = $resource("http://localhost:9998/realestates/", {callback: "JSON_CALLBACK"}, {get:{method:"JSONP"}});
//    $scope.realEstates = $scope.searchApi.get();
//    
    var url = "http://127.0.0.1:9998/realestates/";

    $http.get(url)
        .success(function(data, status, headers, config) {
            $scope.realEstates = data;
            $scope.pagination.numPages = Math.ceil($scope.realEstates.length/$scope.pagination.perPage);
        })
        .error(function(data, status, headers, config) {
            console.log(data);
        });
    
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