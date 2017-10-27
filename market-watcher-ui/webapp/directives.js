myApp.directive("searchResult", function() {
	return {
		restrict: "AECM",
		templateUrl: "directives/search-result.html",
		replace: true,
		scope: {
			realEstateObject: "=",
			formattedRealEstateFunction: "&"
		},
		link: function(scope, elements, attrs) {
			console.log(elements);
		},
		transclude: true
	}
});

myApp.directive("subscriptionList", function() {
	return {
		restrict: "AECM",
		templateUrl: "directives/subscription-list.html",
		replace: true,
		scope: {
			subscriptionObject: "="
		},
		link: function(scope, elements, attrs) {
			console.log(elements);
		},
		transclude: true
	}
})
