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


app.controller('gameListController',function($scope,$http,$window){
    $scope.games={};
    $scope.Math=$window.Math;
    $scope.page=1;
    var get_games=function(page){
        $scope.loading=true;
        $http.get('/chessdb/games?page='+page.toString()).success(function(data){
    	    console.log(data);
    	    $scope.games=data;
            $scope.loading=false;
        });
    };
    $scope.get_prev=function(){
        $scope.page=$scope.page-1;
        get_games($scope.page);
    };
    $scope.get_next=function(){
        $scope.page=$scope.page+1;
        get_games($scope.page);
    };
    get_games($scope.page);
});

app.controller('gameDetailController',function($scope,Game){
    $scope.init=function(game_id)
    {
    	$scope.game=new Game();
    	$scope.game.id=game_id;
        $scope.arrow="M149,263 L296,283";
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
        var move=$scope.game.moves[tempo+1];
    	$scope.board.position(move.fen);
        $scope.drawArrow(move.from,move.to);
    };

    $scope.drawArrow=function(from,to)
    {
        console.log($("#board"));
        board=$("#board")[0]
        offsetLeft=board.offsetLeft
        offsetTop=board.offsetTop
        square_from=$("div[data-square='" + from + "']")[0]
        square_to=$("div[data-square='" + to + "']")[0]
        xini=square_from.offsetLeft - offsetLeft + square_from.offsetWidth/2.;
        yini=square_from.offsetTop - offsetTop + square_from.offsetHeight/2. +4 ;
        xfin=square_to.offsetLeft - offsetLeft + square_to.offsetWidth/2.;
        yfin=square_to.offsetTop - offsetTop + square_to.offsetHeight/2 +4;
        m=(yfin-yini)/(xfin-xini);
        n=yfin-m*xfin;
        ynew=(yfin-yini)*0.95+yini;
        xnew=(xfin-xini)*0.95+xini;
        $scope.arrow="M"+xini+","+yini+" L"+xnew+","+ynew;

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

