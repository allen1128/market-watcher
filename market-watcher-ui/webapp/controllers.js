myApp.controller('searchController', ['$scope', '$filter', '$resource', '$http', '$location', 'searchService', 'Pagination', function($scope, $filter, $resource, $http, $location, searchService, Pagination) {
    var PAGE_SIZE = 10;
    $scope.pagination = Pagination.getNew(PAGE_SIZE);

    $http.get('assets/results.json')
        .success(function(result) {
            $scope.realEstates = result;
            $scope.pagination.numPages = Math.ceil($scope.realEstates.length / $scope.pagination.perPage);
        })
        .error(function(data, status) {
            console.log(data);
        });
    //
    //    $scope.searchApi = $resource("http://localhost:9998/realestates/", {callback: "JSON_CALLBACK"}, {get:{method:"JSONP"}});
    //    $scope.realEstates = $scope.searchApi.get();
    //    
    //var url = "http://127.0.0.1:9998/realestates/";

    // $http.get(url)
    //     .success(function(data, status, headers, config) {
    //         $scope.realEstates = data;
    //         $scope.pagination.numPages = Math.ceil($scope.realEstates.length / $scope.pagination.perPage);
    //     })
    //     .error(function(data, status, headers, config) {
    //         console.log(data);
    //     });

    $scope.formattedRealEstate = function(realEstate) {
        return 'price: ' + realEstate.price + ', number of bedrooms:' + realEstate.bedroomNr + ', neighbood:' + realEstate.hood + ', posted date: ' + realEstate.postedDate;
    }
}]);

myApp.controller('forecastController', ['$scope', '$routeParams', function($scope, $routeParams) {
    $scope.name = "forecast page";
    $scope.num = $routeParams.num;
}]);

myApp.controller('notificationController', ['$scope', 'Pagination', function($scope, Pagination) {
    var PAGE_SIZE = 1;
    $scope.pagination = Pagination.getNew(PAGE_SIZE);

    $scope.selectedCity = "",
        $scope.cities = [
            {
                id: 1, name: "Montreal"
            },
            {
                id: 2, name: "Toronto"
            },
            {
                id: 3, name: "Vancouver"
            }
        ];
    $scope.priceRange = [
        {
            id: 1, name: "100K"
        }, {
            id: 2, name: "300K"
        }, {
            id: 3, name: "500K"
        }, {
            id: 4, name: "700K"
        }, {
            id: 5, name: "900K"
        }, {
            id: 6, name: "1M"
        }, {
            id: 7, name: "1.5M"

        }, {
            id: 7, name: "Any"
        }
    ];
    $scope.roomNrRange = [
        {
            id: 1, name: "1br"
        }, {
            id: 2, name: "2br"
        }, {
            id: 3, name: "3br"
        }, {
            id: 4, name: "4br"
        }, {
            id: 5, name: "Any"
        }
    ];

    $scope.subscriptions = [{ "email": "abc@gmail.com" }, { "email": "bill.gates@microsoft.com" }]
    $scope.pagination.numPages = Math.ceil($scope.subscriptions.length / $scope.pagination.perPage);

}]);

myApp.controller('mainController', ['$scope', '$filter', '$http', '$location', function($scope, $filter, $http, $location) {
    $scope.searchKeyword = '';
    $scope.characters = 3;
    $scope.lowercasesearchkeyword = function() {
        return $filter('lowercase')($scope.searchKeyword);
    }
}]);
