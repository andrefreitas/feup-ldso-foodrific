$(document).ready(function(){
	$('#register').click(function(){
		registerClick();
	});

	$('#login').click(function(){
		loginClick();
	});
})

var PASSWORDS_MINIMUM_LENGTH = 5;
/**
* When someone clicks on the register button
**/
function registerClick(){
	$("#banner").fadeOut(400, function(){
		$("#banner").remove();
		$('#registerForm').css("display", "block");
	});	
}

/** 
* Validate the registration form
**/
function validateRegisterForm(){
	var fields = $('#registerForm form').serializeArray();
	var name = fields[0]["value"],
		email = fields[1]["value"],
		birthday = fields[2]["value"],
		gender = fields[3]["value"],
		password = fields[4]["value"],
		passwordConfirm = fields[5]["value"];

	$(".alert").html("");	

	if(!nameIsValid(name)){
		$("#nameAlert").html("Nome inválido!").effect("shake");
		return false;
	}

	if(!emailIsValid(email)){
		$("#emailAlert").html("Email inválido!").effect("shake");
		return false;
	}
	if(!dateIsValid(birthday)){
		$("#birthdayAlert").html("Data de nascimento inválida!").effect("shake");
		return false;
	}

	if(!genderIsValid(gender)){
		$("#genderAlert").html("Não escolheu um gênero!").effect("shake");
		return false;
	}

	if(!passwordsAreValid(password,passwordConfirm)){
		if(password.length < 5)
			$("#passwordAlert").html("A password tem que ter pelo menos 5 caracteres!").effect("shake");
		else 
			$("#passwordConfirmAlert").html("As passwords não são iguais!").effect("shake");
		return false;
	}

	return true;
}

/** Validations **/
function nameIsValid(name){
	return name.length > 1;
}

/** Email Validation 
* http://stackoverflow.com/questions/46155/validate-email-address-in-javascript
**/
function emailIsValid(email){
	var re = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(email);
}

/** Date Validation **/

function dateIsValid(date){
	var re = /^[0-3]?[0-9]\/[01]?[0-9]\/[12][90][0-9][0-9]$/;
	return re.test(date);
}

/** Gender validation **/
function genderIsValid(gender){
	return gender == "m" || gender == "f";
}

/** Validate Passwords **/
function passwordsAreValid(password, passwordConfirm){
	return password.length >= PASSWORDS_MINIMUM_LENGTH && password == passwordConfirm;
}

/** Login Click **/

function loginClick(){
	$("#banner").fadeOut(400, function(){
		$("#banner").remove();
		$('#loginForm').css("display", "block");
	});	
}