var module = angular.module('game.services', ['ngResource']);

module.factory('Game',['$resource',function($resource){
	return $resource('/chessdb/games/:id', {id: '@id'},{
           update: {method:'PUT', params: {id: '@id',data:'@data'}},
           create: {method:'POST'},
           list: {method:'GET', url:'/api/material_solic'},
           get_filters: {method:'GET', url:'/api/material_solic/?:data', params: {data:'@data'}},
        });
}]);
