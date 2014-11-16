var app=angular.module('app.game.list',['ngCookies','game.services']);

app.config(function($interpolateProvider,$httpProvider){
	$interpolateProvider.startSymbol('{$');
	$interpolateProvider.endSymbol('$}');
	$httpProvider.defaults.headers.post['Content-Type'] = 'application/json';
	$httpProvider.defaults.xsrfCookieName = 'csrftoken';
	$httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
	
}).run(['$http','$cookies',function($http,$cookies){
	$http.defaults.headers.post['X-CSRFToken']=$cookies.csrftoken;
}]);


app.controller('gameListController',function($scope,$http){
    $scope.games={};
    $http.get('/chessdb/games').success(function(data){
    	$scope.games=data;
    });
});

app.controller('gameDetailController',function($scope,Game){
    $scope.init=function(game_id)
    {
    	$scope.game=new Game();
    	$scope.game.id=game_id;
    	$scope.game.$get().then(function(data){
	    	var cfg = {
	            draggable: true,
	            position: $scope.game.moves[0].fen,
	            pieceTheme: '/static/img/chesspieces/wikipedia/{piece}.png'
	        };
	        $scope.tempo = -1;
        	$scope.board = new ChessBoard('board', cfg);    		
    	});
    };
    $scope.update_tempo=function(tempo)
    {
    	$scope.tempo=tempo;
    	$scope.board.position($scope.game.moves[tempo+1].fen);
    };

    $scope.key_down=function($event)
    {
        if ($event.keyCode==39 || $event.keyCode==40){
        	$scope.inc_tempo();
        }
        if ($event.keyCode==37 || $event.keyCode==38){
        	$scope.dec_tempo();
        }
    };

    $scope.inc_tempo=function()
    {
    	if ($scope.tempo < $scope.game.moves.length-2){
    		$scope.update_tempo($scope.tempo+1);

    	}

    }

    $scope.dec_tempo=function()
    {
    	if ($scope.tempo > -1){
    		$scope.update_tempo($scope.tempo-1);

    	}

    }



});

