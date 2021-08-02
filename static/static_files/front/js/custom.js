

$(function(){

	function check(){
		var items = $('.alert-class');
		if(items.length > 0){
			setTimeout(function(){
				$('.alert-class').slideUp('slow');
			},3000);
		}	
	}
	check();

});