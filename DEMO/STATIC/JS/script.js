var app=angular.module("app",[]);
 
function PruebaController($scope) {
	$scope.mensaje="Hola Mundo";
}

function HoraControler ($scope) {
	var updateclock = function(){
		var h = new Date()
		$scope.clock = h.getHours()+
			':'+h.getMinutes()+
			':'+h.getSeconds();
	};
	var timer = setInterval( 
		function(){
			$scope.$apply(updateclock)
		},1000);
	updateclock();
}

function ContController($scope){
	$scope.cont = 0
	$scope.add = function(parm){
		$scope.cont += parm;
	};
	$scope.subtract = function(parm){
		$scope.cont -= parm; 
	};
}
// var app=angular.module("app",[]) // <-- This is the getter function for a module previously defined
// .run(function($rootScope) {
// $rootScope.user = {
// email: 'ari@fullstack.io'
// }
// });