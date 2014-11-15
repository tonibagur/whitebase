var app=angular.module('app.game.list',['ngCookies']);

app.config(function($interpolateProvider,$httpProvider){
	$interpolateProvider.startSymbol('{$');
	$interpolateProvider.endSymbol('$}');
	$httpProvider.defaults.headers.post['Content-Type'] = 'application/json';
	$httpProvider.defaults.xsrfCookieName = 'csrftoken';
	$httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
	
}).run(['$http','$cookies',function($http,$cookies){
	$http.defaults.headers.post['X-CSRFToken']=$cookies.csrftoken;
}]);


app.controller('gameListController',function($scope){
    $scope.test='hola';
});

