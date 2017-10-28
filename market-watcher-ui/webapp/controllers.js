myApp.controller('searchController', ['$scope', '$filter', '$resource', '$http', '$location', 'searchService', 'Pagination', function($scope, $filter, $resource, $http, $location, searchService, Pagination) {
    var PAGE_SIZE = 10;
    $scope.pagination = Pagination.getNew(PAGE_SIZE);

    // $http.get('assets/results.json')
    //     .success(function(result) {
    //         $scope.realEstates = result;
    //         $scope.pagination.numPages = Math.ceil($scope.realEstates.length / $scope.pagination.perPage);
    //     })
    //     .error(function(data, status) {
    //         console.log(data);
    //     });
    //
    //    $scope.searchApi = $resource("http://127.0.0.1:9998/realestates/", {callback: "JSON_CALLBACK"}, {get:{method:"JSONP"}});
    //    $scope.realEstates = $scope.searchApi.get();
    
    var url = "http://127.0.0.1:9998/realestates/";

    $http.get(url)
        .success(function(data, status, headers, config) {
            $scope.realEstates = data;
            $scope.pagination.numPages = Math.ceil($scope.realEstates.length / $scope.pagination.perPage);
        })
        .error(function(data, status, headers, config) {
            console.log(data);
        });

    $scope.formattedRealEstate = function(realEstate) {
        return 'price: ' + realEstate.price + ', number of bedrooms:' + realEstate.bedroomNr + ', neighbood:' + realEstate.hood + ', posted date: ' + realEstate.postedDate;
    }
}]);

myApp.controller('forecastController', ['$scope', '$routeParams', function($scope, $routeParams) {
    $scope.name = "forecast page";
    $scope.num = $routeParams.num;
}]);

myApp.controller('notificationController', ['$scope', 'Pagination', '$http', function($scope, Pagination, $http) {
    var PAGE_SIZE = 10;
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
            id: 1, name: "100000"
        }, {
            id: 2, name: "300000"
        }, {
            id: 3, name: "500000"
        }, {
            id: 4, name: "700000"
        }, {
            id: 5, name: "900000"
        }, {
            id: 6, name: "1000000"
        }, {
            id: 7, name: "1500000"
        }
    ];
    $scope.roomNrRange = [
        {
            id: 1, name: "1"
        }, {
            id: 2, name: "2"
        }, {
            id: 3, name: "3"
        }, {
            id: 4, name: "4"
        }, {
            id: 5, name: "5"
        }
    ];

    //$scope.subscriptions = [{ "email": "abc@gmail.com" }, { "email": "bill.gates@microsoft.com" }]

    
    $scope.generateSubscriptionData = function(){
        return {
            "email": $scope.email,
            "city": $scope.city,
            "minPrice": $scope.minPrice,
            "maxPrice": $scope.maxPrice,
            "minRoomNr": $scope.minRoomNr,
            "maxRoomNr": $scope.maxRoomNr
        };
    };

    $scope.addSubscription = function(){
        var url = "http://127.0.0.1:9998/realestates/notification/add/";
        $http.post(url, $scope.generateSubscriptionData())
        .success(function(data){
            $scope.successMsg = "Added Successfully";
            $scope.getSubscriptions();
        })
        .error(function(data){
            console.log(data);
        });
    };

    $scope.getSubscriptions = function(){
        var url = "http://127.0.0.1:9998/realestates/notifications/";
        $http.get(url)
        .success(function(data, status, headers, config) {
            $scope.subscriptions = data;
            $scope.pagination.numPages = Math.ceil($scope.subscriptions.length / $scope.pagination.perPage);
        })
        .error(function(data, status, headers, config) {
            console.log(data);
        });
    };

    $scope.getSubscriptions();

}]);

myApp.controller('mainController', ['$scope', '$filter', '$http', '$location', function($scope, $filter, $http, $location) {
    $scope.searchKeyword = '';
    $scope.characters = 3;
    $scope.lowercasesearchkeyword = function() {
        return $filter('lowercase')($scope.searchKeyword);
    }
}]);
