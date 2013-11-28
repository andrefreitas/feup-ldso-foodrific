//Global variables jQuery
window.toDelete;

$(document).ready(function(){

	$('#register').click(function(){
		registerClick();
	});

	$('#login').click(function(){
		loginClick();
	});

	$('#addPost').click(function(){
		addPostClick();
	});

	$('#publishPost').click(function(){
		publishPostClick();
	});
	
	$('.recoverPasswordButton').click(function(){
		recoverPasswordPopUp();
	});

	$('.deletePost').click(function(){
		deletePostClick(this);
	});
	
	$('.yummyAction').click(function(){
		yummyClick(this);
	});

	$("#uploadImage").change(function(){
    	readImageURL(this);
	});

	$('#tags').tagsInput({	
	'height':'',
	'width':'',
	'color':'',
	'defaultText':'Novo Ingrediente',	
	'placeholderColor' : '#AAAAAA',
	'autocomplete_url' : 'api/ing_tags',
	'autocomplete':{
			selectFirst:true,
			autoFill:true, 
			delay: 250, 
			minLength: 3
		}
	});

	$('.comments').click(function(){
		showCommentsClick(this);
	});

	$('.addComment').click(function(){
		addCommentClick(this);
	});

});

var PASSWORDS_MINIMUM_LENGTH = 5;

/**
* When someone clicks on the register button
**/
function registerClick(){
	window.location.assign("/register")
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

	if(!registerIsValid(email)) {
		$("#emailAlert").html("O email não é válido!").effect("shake");
		return false;
	}

	else return true;
}

function registerIsValid(email){
	 $.ajaxSetup( { "async": false } );
     var data = $.getJSON("api/register_verification",{
            email: email
     });
    $.ajaxSetup( { "async": true } );
    return $.parseJSON(data["responseText"])["answer"] == 'valid' ;
}

function validateRecoveryPasswordForm(){
	var fields = $('#passwordForm form').serializeArray();
	var password = fields[1]["value"],
		passwordConfirm = fields[2]["value"];

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
	window.location.assign("/login")
}

function validateLoginForm(){
	var fields = $('#loginForm form').serializeArray();
	var email = fields[0]["value"],
		password = fields[1]["value"];

	$(".alert").html("");	

	if(!emailIsValid(email)){
		if(email.length ==0)
			$("#emailLoginAlert").html("Escreva o email!").effect("shake");
		else
			$("#emailLoginAlert").html("Email inválido!").effect("shake");
		return false;
	}

	if(password.length == 0){
		$("#passwordLoginAlert").html("Escreva a password!").effect("shake");
	}
	if(loginIsValid(email, password))
		return true;
	$("#emailLoginAlert").html("Login errado!").effect("shake");
	return false;
}

function validateEmail()
{
	var email = $('#recoverPasswordForm [name=emailToRecover]').val();

	if(!emailIsValid(email))
	{
		if(email.length ==0)
		{
			$("#recoverPasswordAlert").html("Escreva o email!").effect("shake");
		}
		else
		{
			$("#recoverPasswordAlert").html("Email inválido!").effect("shake");
		}

		return false;
	}
	else
	{
		if(emailDatabaseIsValid(email))
		{
			return true;
		}
		else
		{
			$("#recoverPasswordAlert").html("Email inválido!").effect("shake");
			return false;
		}
	}
}

function emailDatabaseIsValid(email)
{
	$.ajaxSetup( { "async": false } );
     var data = $.getJSON("api/send_recover",{
            email: email
     });
    $.ajaxSetup( { "async": true } );
    return $.parseJSON(data["responseText"])["answer"] == 'valid' ;
}

function loginIsValid(email, password){
	 $.ajaxSetup( { "async": false } );
     var data = $.getJSON("api/login",{
            email: email,
            password: password
     });
    $.ajaxSetup( { "async": true } );
    return $.parseJSON(data["responseText"])["answer"] == 'valid' ;
}

function addPostClick(){
	if($("#newPost").is(':visible'))
		$("#newPost").fadeOut();
	else
		$("#newPost").fadeIn();
}

function readImageURL(input) {

    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#foodImage').attr('src', e.target.result);
        }

        reader.readAsDataURL(input.files[0]);
    }else{
    	$('#foodImage').attr('src', 'images/post-photo.svg');
    }
}

function validatePublishPost(){
	var fields = $('#newPost form').serializeArray();
	var title = fields[0]["value"];

	$(".alert").html("");	
	if(title.length < 1){
		$("#titleAlert").html("Escreva um título!").effect("shake");
		return false;
	}
	var imgVal = $('#uploadImage').val(); 
    if(imgVal=='') 
    { 
        $("#photoAlert").html("Insira uma imagem!").effect("shake");
        return false; 
    }   
	
}

function deletePost(id_post){
	$.ajaxSetup( { "async": false } );
     var data = $.getJSON("api/delete_post",{
            postId: id_post
     });
    $.ajaxSetup( { "async": true } );
    console.log("Called api/delete_post?postId="+id_post);
    console.log($.parseJSON(data["responseText"]));
    var postBox = $('#'+ id_post);
	$(postBox).attr("class", "");
	$(postBox).html("");
    if($.parseJSON(data["responseText"])["answer"] == 'valid'){
		addNotification(postBox, 'O post foi eliminado!', "confirmation");
    } else {
    	addNotification(postBox, 'Falhou a eliminar :(', "error");
    }
}



function getPostId(action){
	var post = $(action).parent().parent();
	var postId = post.attr("id");
	return postId;
}

function getPostYummys(action) {
	var Yummys = $(action).children().children('.text').first().html();
	Yummys = Yummys.split(" ");
	Yummys = parseInt(Yummys[0]);
	return Yummys;
}

function setPostYummys(action, Yummys) {
	
	$(action).children().children('.text').first().html(Yummys + (Yummys != 1?" yummys":" yummy"));
}

function isPostYummi(action) {
	return $(action).attr("id") == "done";
}

function setPostYummiIcon(action, status) {
	var imgDone = "images/yummy-done.svg";
	var imgUndone = "images/yummy.svg";
	if(status) {
		$(action).children(".action").first().children().first().attr("src", imgDone);
		$(action).attr("id", "done");
	} else {
		$(action).children(".action").first().children().first().attr("src", imgUndone);
		$(action).attr("id", "undone");
	}
}

function yummyClick(action){
	var postId = getPostId(action);
	var Yummys = getPostYummys(action);
	var isDone = isPostYummi(action);
	if(isDone) {
		setPostYummys(action, Yummys - 1);
		setPostYummiIcon(action, false);
	} else {
		setPostYummys(action, Yummys + 1);
		setPostYummiIcon(action, true);
	}
    
	addYummy(postId);
}

function addYummy(postId){
	$.ajaxSetup( { "async": false } );
    var data = $.getJSON("api/yummy",{
            postId: postId
     });
    $.ajaxSetup( { "async": true } );
    console.log("Called api/yummy?postId="+postId)
    console.log($.parseJSON(data["responseText"]));
    return $.parseJSON(data["responseText"])["answer"] == 'done' ;
}

function recoverPasswordPopUp(){
	$('#recoverPasswordForm').bPopup({
	    easing: 'easeOutBack', //uses jQuery easing plugin
       	speed: 450,
        transition: 'slideDown'
    });
}

function deletePostClick(elem) {
	$('#questionPopUp').bPopup({
	    easing: 'easeOutBack', //uses jQuery easing plugin
       	speed: 450,
       	transition: 'slideDown'
    });
	var father = $(elem).parent().parent().parent();
	var id_post = father.attr("id");
	toDelete = id_post;
}

function deletePostYes(){
	$('#questionPopUp').bPopup().close();
	deletePost(toDelete);
}

function deletePostNo(){
	$('#questionPopUp').bPopup().close();
}

function addNotification(parentElement, text, type){
	var confirmation = '<div class="notification ' + type + '">' + text + '<img src="images/close-white.svg"></div>';
	$(parentElement).append(confirmation);
	$('.notification').fadeIn();
	$('.notification').click(function(){
		$(this).remove();
	});

}

function showCommentsClick(elem){
	var commentSection = $(elem).parent().parent().children(".commentSection");
	if($(commentSection).is(':visible'))
		$(commentSection).fadeOut();
	else
		$(commentSection).fadeIn();
}

function addCommentClick(elem){
	var comment = $(elem).parent().children('textarea').val();
	var postID = $(elem).parent().parent().attr("id");
	$(elem).parent().children('textarea').val("");
	if(comment.length > 0) {
		requestAddComment(postID, comment);
	}
}

function addCommentUI(postId, author, comment, commentId, time) {
	var comment = '<div class="comment" id="' + commentId +'">'
				+ '<div class="commentText"><span class="author">' + author + '</span>'
				+ comment + '</div>'
				+ '<span class="time">' + time + '</span></div>';
	$('.post#'+postId).children('.commentSection').children('.commentsUpdates').prepend(comment);
}

function requestAddComment(postId, comment) {
	var url = "api/new_comment";
    $.getJSON(url,{
            postId: postId,
            comment : comment
     }).done(function(data){
     	var author = getSessionData()["name"];
     	addCommentUI(postId, author, comment, "2323212123", "agora mesmo");
     });
    $.ajaxSetup( { "async": true } );
    console.log("Called " + url + "?postId="+  postId + "&comment=" + comment);
}

function getSessionData(){
	var url = "api/session_data";
	$.ajaxSetup( { "async": false } );
    var data = $.getJSON(url);
    $.ajaxSetup( { "async": true } );
    return $.parseJSON(data["responseText"])["answer"];
}