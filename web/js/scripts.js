$(document).ready(function(){
	$('#register').click(function(){
		registerClick();
	});
})
/**
* When someone clicks on the register button
**/
function registerClick(){
	$("#banner").fadeOut(400, function(){
		$("#banner").remove();
		$('#registerForm').css("display", "block");
	});
	
}