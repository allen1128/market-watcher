myApp.directive("searchResult", function(){
	return {
		restrict: 'AECM',
		templateUrl: 'directives/search-result.html',
		replace: true,
		scope: {
			realEstateObject: "=",
			formattedRealEstateFunction: "&"
		},
		link: function(scope, elements, attrs){
			console.log(elements);
		},
		transclude: true
	}
});
