//Global variables jQuery
window.toDelete;
window.comment_id;
window.post_id;

$(document).ready(function(){
	$( "#datepicker" ).datepicker({
		showButtonPanel: true,
		changeMonth: true,
		changeYear: true,
		yearRange:'-90:-12',
		defaultDate: '-12Y',
		reverseYearRange: true,
		closeText: 'Fechar',
		prevText: '&#x3c;Anterior',
		nextText: 'Seguinte',
		currentText: 'Hoje',
		monthNames: ['Janeiro','Fevereiro','Mar&ccedil;o','Abril','Maio','Junho',
		'Julho','Agosto','Setembro','Outubro','Novembro','Dezembro'],
		monthNamesShort: ['Jan','Fev','Mar','Abr','Mai','Jun',
		'Jul','Ago','Set','Out','Nov','Dez'],
		dayNames: ['Domingo','Segunda-feira','Ter&ccedil;a-feira','Quarta-feira','Quinta-feira','Sexta-feira','S&aacute;bado'],
		dayNamesShort: ['Dom','Seg','Ter','Qua','Qui','Sex','S&aacute;b'],
		dayNamesMin: ['Dom','Seg','Ter','Qua','Qui','Sex','S&aacute;b'],
		weekHeader: 'Sem',
		dateFormat: 'dd/mm/yy'
	});
	
	$('#register').click(function(){
		registerClick();
	});

	$('#login').click(function(){
		loginClick();
	});

	$('#addPost').click(function(){
		addPostClick();
	});

	$('.text_share').click(function(){
		var id_post = $(this).parent().parent().parent().attr("id");
		showShareIcons(id_post);
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

	$('.deleteUser').click(function(){
		deleteUserClick(this);
	});

	$('.editPost').click(function(){
		editPostClick(this);
	});

	$('#editProfileBt').click(function(){
		window.location = "show_profile"
	});

	$('#newPost #tags').tagsInput({	
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

	$('#newPost input#tags_tag').keyup(function(){
		delimiterTags();
	});
	
	$('.yummyAction').click(function(){
		yummyClick(this);
	});

	$("#uploadImage").change(function(){
    	readImageURL(this);
	});

	$('.comments').click(function(){
		showCommentsClick(this);
	});

	$('.recipe').click(function(){
		showRecipeClick(this);
	});

	$('.addComment').click(function(){
		addCommentClick(this);
	});

	$('.comment .delete').click(function(){
		deleteCommentClick(this);
	});

	$('#followBt').click(function(){
		followClick(this);
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
* Validate editForms
**/
function validateEditNameForm(){
	var name = $('#editNameField').val();

	if(!nameIsValid(name)){
		$("#nameAlert").html("Nome inválido!").effect("shake");
		return false;
	}

	return true;
}

function validateEditEmailForm(){
	var email = $('#editEmailField').val();

	if(!emailIsValid(email)){
		$("#emailAlert").html("Email inválido!").effect("shake");
		return false;
	}

	return true;
}

function validateEditBirthdayForm(){
	var birthday = $('#editBirthdayField').val();

	if(!dateIsValid(birthday)){
		$("#birthdayAlert").html("Data de nascimento inválida!").effect("shake");
		return false;
	}

	return true;
}

function validateEditPasswordForm(){
	oldPassword = $('#editOldPasswordField').val();
	password = $('#editNewPasswordField').val();
	passwordConfirm = $('#editConfNewPasswordField').val();

	if(!passwordIsValid(oldPassword)) {
		$("#oldPasswordAlert").html("Password atual inválida!").effect("shake");
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

function passwordIsValid(password){
	$.ajaxSetup( { "async": false } );
     var data = $.getJSON("api/verifyPassword",{
            password: password
     });
    $.ajaxSetup( { "async": true } );
    return $.parseJSON(data["responseText"])["answer"] == 'valid' ;
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
	
	return true;
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
	if($("#newPost").is(':visible')){
		$("#newPost").fadeOut();
	}
	else{
		$("#newPost").fadeIn();
	}
}

function showShareIcons(id_post){
	if($("#" + id_post + " .social").is(':visible')){
		$("#" + id_post + " .social").fadeOut();
	}
	else{
		$("#" + id_post + " .social").fadeIn();
	}
}

function readImageURL(input) 
{
	var imgVal = $('#uploadImage').val();

	$("#photoAlert").html("");
	var extension = imgVal.substring(imgVal.lastIndexOf('.') + 1).toLowerCase();
    if (extension != "gif" && extension != "png" && extension != "bmp" && extension != "jpeg" && extension != "jpg")
    {
    	$("#photoAlert").html("Insira uma imagem válida!").effect("shake");
    }
    else if (input.files && input.files[0]) {
        
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#foodImage').attr('src', e.target.result);
        }

        reader.readAsDataURL(input.files[0]);
    }else{
    	$('#foodImage').attr('src', 'images/post-photo.svg');
    }    
}

function readImageURLEdit(input, id_post) 
{
	var imgVal = $(".editPost" + id_post + " #uploadImageEdit").val();

	$(".editPost" + id_post + " #photoAlert").html("");
	var extension = imgVal.substring(imgVal.lastIndexOf('.') + 1).toLowerCase();
    if (extension != "gif" && extension != "png" && extension != "bmp" && extension != "jpeg" && extension != "jpg")
    {
    	$(".editPost" + id_post + " #photoAlert").html("Insira uma imagem válida!").effect("shake");
    }
    else if (input.files && input.files[0]) {
        
        var reader = new FileReader();

        reader.onload = function (e) {
            $(".editPost" + id_post + " #foodImage").attr('src', e.target.result);
        }

        reader.readAsDataURL(input.files[0]);
    }else{
    	$(".editPost" + id_post + " #foodImage").attr('src', 'images/post-photo.svg');
    }    
}

function delimiterTags()
{
	var str_tag = $('#newPost input#tags_tag').val();

	if(str_tag.length > 8)
	{
		$('#newPost input#tags_tag').val(str_tag.substring(0, str_tag.length-1));
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
    var extension = imgVal.substring(imgVal.lastIndexOf('.') + 1).toLowerCase();
    if (extension != "gif" && extension != "png" && extension != "bmp" && extension != "jpeg" && extension != "jpg")
    {
    	$("#photoAlert").html("Insira uma imagem válida!").effect("shake");
    	return false;
    }
}

function validateEditPost(id_post)
{
	var fields = $(".editPost" + id_post + " form").serializeArray();
	var title = fields[1]["value"];

	$(".editPost" + id_post + " .alert").html("");	
	if(title.length < 1){
		$(".editPost" + id_post + " #titleAlert").html("Escreva um título!").effect("shake");
		return false;
	}
	var imgVal = $(".editPost" + id_post + " #uploadImageEdit").val();
	
	if(imgVal != '')
	{ 
	    var extension = imgVal.substring(imgVal.lastIndexOf('.') + 1).toLowerCase();
	    if (extension != "gif" && extension != "png" && extension != "bmp" && extension != "jpeg" && extension != "jpg")
	    {
	    	$(".editPost" + id_post + " #photoAlert").html("Insira uma imagem válida!").effect("shake");
	    	return false;
	    }
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

function editPost(id_post)
{
	$('#posts #' + id_post).hide();

	$.ajaxSetup( { "async": false } );
     var data = $.getJSON("api/get_post",{
            postId: id_post
     });

    var numTag = Math.floor((Math.random()*100000000000000000)+1);

    var resultEditPost = $.parseJSON(data["responseText"]);
    console.log("Called api/get_post?postId="+id_post);
    console.log(resultEditPost);

    if(resultEditPost["result"] == "ok")
    {
    	console.log("Faz bem!!");

    	var $header = $('.editPost' + id_post);
    	var $form_header = $('<form id="editpost" method="post" action="api/edit_post" onsubmit="return validateEditPost(' + id_post + ')" enctype="multipart/form-data">').appendTo($header);
    	$('<input type="hidden" name="postId" value="'+ id_post +'" />').appendTo($form_header);
    	$('<div class="alert" id="titleAlert"></div>').appendTo($form_header);
    	$('<input type="text" name="title" placeholder="Qual é o título?" value="'+ resultEditPost["title"] +'"/> <br/>').appendTo($form_header);
    	var $divPhoto = $('<div class="photo">').appendTo($form_header);
    	$('<img id="foodImage" src="/api/postimage?id='+ id_post +'" alt="Imagem do prato">').appendTo($divPhoto);
    	$('</div>').appendTo($form_header);
    	$('<div class="alert" id="photoAlert"></div>').appendTo($form_header);
    	var $fileInputs = $('<div class="fileinputs">').appendTo($form_header);
    	$('<input type="file" name="photo" id="uploadImageEdit" class="file" />').appendTo($fileInputs);
    	$('<button class="fakefile" id="addImage"> Adicionar Imagem </button>').appendTo($fileInputs);
    	$('</div>').appendTo($form_header);
    	$('<div class="alert" id="ingredientsAlert"></div>').appendTo($form_header);
    	
    	if(resultEditPost["ingredients"] == "")
    	{
    		$('<input name="ingredients" id="tagsEdit'+ numTag +'"/>').appendTo($form_header);
    	}
    	else if(resultEditPost["ingredients"].length != "")
    	{
    		var values = "";
    	    
    	    for(var i = 0; i < resultEditPost["ingredients"].length; i++)
    		{
    			if(i == 0)
    			{
    				values = resultEditPost["ingredients"][i];
    			}
    			else
    			{
    				values = values + "," + resultEditPost["ingredients"][i];
    			}
    		}

    		$('<input name="ingredients" id="tagsEdit'+ numTag +'" value="'+ values +'">').appendTo($form_header);
	    }

	    if(resultEditPost["recipe"] == null)
    	{
    		$('<textarea name="recipe" placeholder="Qual é a receita?" rows="3" cols="50" form="editpost"></textarea> <br/>').appendTo($form_header);
    	}
    	else
    	{
        	$('<textarea name="recipe" placeholder="Qual é a receita?" rows="3" cols="50" form="editpost">'+ resultEditPost["recipe"] + '</textarea> <br/>').appendTo($form_header);
        }
        $('<input type="submit" value="Alterar" class="orange"/>').appendTo($form_header);
        $('<input type="button" value="Cancelar" class="blue" onclick="return cancelEdit('+ id_post +')"/>').appendTo($form_header);
        $('</form>').appendTo($header);

        $('#posts #' + id_post).siblings("#posts .editPost"+ id_post).show();
        
        if(resultEditPost["ingredients"] != "")
        {
	        $('#editPost #tagsEdit' + numTag).tagsInput({	
				'height':'',
				'width':'',
				'color':'',
				'defaultText':'',	
				'placeholderColor' : '#AAAAAA',
				'autocomplete_url' : 'api/ing_tags',
				'autocomplete':{
						selectFirst:true,
						autoFill:true, 
						delay: 250, 
						minLength: 3
					}
			});
    	}
    	else if(resultEditPost["ingredients"] == "")
        {
	        $('#editPost #tagsEdit' + numTag).tagsInput({	
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
    	}

		$('#editPost input#tagsEdit' + numTag +'_tag').css("border", "none");
		$('#editPost input#tagsEdit' + numTag +'_tag').css("font-size", "24px");
		$('#editPost input#tagsEdit' + numTag +'_tag').css("width", "250px");
		$('#editPost input#tagsEdit' + numTag +'_tag').css("margin-bottom", "5px");
		$('#editPost input#tagsEdit' + numTag +'_tag').css("font-family", "'Verdana', sans-serif");
		$('#editPost input#tagsEdit' + numTag +'_tag').keyup(function(event)
		{
			var str_tag = $('#editPost input#tagsEdit' + numTag +'_tag').val();

			if(str_tag.length > 8)
			{
				$('#editPost input#tagsEdit' + numTag +'_tag').val(str_tag.substring(0, str_tag.length-1));
			}
		});

		$(".editPost" + id_post + " #uploadImageEdit").change(function(){
    		readImageURLEdit(this, id_post);
		});
    }
}

function cancelEdit(id_post)
{
	$("#posts .editPost"+ id_post + " #editpost").remove();
	$("#posts .editPost"+ id_post).hide();
	$('#posts #' + id_post).show();
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
	
	$(action).children().children('.text').first().html(Yummys);
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

function editPostClick(elem)
{
	var father = $(elem).parent().parent().parent();
	var id_post = father.attr("id");
	editPost(id_post);
}

function deleteUserClick(elem) {
	$('#questionPopUp').bPopup({
	    easing: 'easeOutBack', //uses jQuery easing plugin
       	speed: 450,
       	transition: 'slideDown'
    });
}

function deleteUserClickAdmin(elem) {
	$('#deleteUserPopUp').bPopup({
	    easing: 'easeOutBack', //uses jQuery easing plugin
       	speed: 450,
       	transition: 'slideDown'
    });
}

function deleteUserNo(){
	$('#questionPopUp').bPopup().close();
	$('#deleteUserPopUp').bPopup().close();
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

function showRecipeClick(elem){
	var recipeSection = $(elem).parent().children(".recipeSection");
	if($(recipeSection).is(':visible'))
		$(recipeSection).fadeOut();
	else
		$(recipeSection).fadeIn();
}

function addCommentClick(elem){
	var comment = $(elem).parent().children('textarea').val();
	comment = stripHTML(comment)
	var postID = $(elem).parent().parent().attr("id");
	$(elem).parent().children('textarea').val("");
	if(comment.length > 0) {
		requestAddComment(postID, comment);
	}
}

function stripHTML(string) {
	var strippedText = $("<div/>").html(string).text();
	return strippedText;
}

function addCommentUI(postId, author, comment, commentId, time) {
	var comment = '<div class="comment" id="' + commentId +'">'
				+ '<div class="commentText"><img src="api/get_avatar"><span class="author">' + author + '</span>'
				+ comment + '</div>'
				+ '<span class="time">' + time + '</span> <span class="delete">eliminar</span></div>';
	$('.post#'+postId).children('.commentSection').children('.commentsUpdates').prepend(comment);
	$('.comment .delete').click(function(){
		deleteCommentClick(this);
	});
}

function requestAddComment(postId, comment) {
	var url = "api/new_comment";
    $.getJSON(url,{
            postId: postId,
            comment : comment
     }).done(function(data){
     	var author = getSessionData()["name"];
     	var commentId = data["comment_id"];
     	console.log(data);
     	addCommentUI(postId, author, comment, commentId, "agora mesmo");
     	incrementCommentsNumberUI(postId, 1);

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

function incrementCommentsNumberUI(postId, value) {
	var commentsText = $("#" + postId).children(".actions").first().children(".comments").first().children(".action").first().children(".text");
	var html = $(commentsText).html();
	var number = parseInt(html.trim().split(" ")[0]);
	number = number + value;
	var sufix = "";
	if(number != 1)
		sufix = "s";
	$(commentsText).html(number);
}

function deleteCommentClick(elem){
	post_id = $(elem).parent().parent().parent().parent().attr("id");
	comment_id = $(elem).parent().attr("id");
	$('#deleteCommentPopUp').bPopup({
	    easing: 'easeOutBack', //uses jQuery easing plugin
       	speed: 450,
       	transition: 'slideDown'
    });
}

function requestDeleteComment(comment_id, post_id) {
	var url = "api/delete_comment";
    $.getJSON(url,{
            comment_id: comment_id
     }).done(function(data){
     	console.log(data);
     	$(".comment#" +comment_id).fadeOut();
     	incrementCommentsNumberUI(post_id, -1);

     });
    console.log("Called " + url + "?comment_id="+  comment_id);
}

function deleteCommentYes(){
	$('#deleteCommentPopUp').bPopup().close();
	requestDeleteComment(comment_id, post_id);
}

function deleteCommentNo(){
	$('#deleteCommentPopUp').bPopup().close();
}

function editName() {
	$('#editName').bPopup({
	    easing: 'easeOutBack', //uses jQuery easing plugin
       	speed: 450,
        transition: 'slideDown'
    });
}

function editEmail() {
	$('#editEmail').bPopup({
	    easing: 'easeOutBack', //uses jQuery easing plugin
       	speed: 450,
        transition: 'slideDown'
    });
}      
function editBirthday() {
	$('#editBirthday').bPopup({
	    easing: 'easeOutBack', //uses jQuery easing plugin
       	speed: 450,
        transition: 'slideDown'
    });
}
function editGender() {
	$('#editGender').bPopup({
	    easing: 'easeOutBack', //uses jQuery easing plugin
       	speed: 450,
        transition: 'slideDown'
    });
}
function editPassword() {
	$('#editPassword').bPopup({
	    easing: 'easeOutBack', //uses jQuery easing plugin
       	speed: 450,
        transition: 'slideDown'
    });
} 

function requestToggleFollow(user_id){
	$.ajaxSetup( { "async": false } );
    var data = $.getJSON("api/toggleFollow",{
            user: user_id
     });
    $.ajaxSetup( { "async": true } );
    console.log("Called api/toggleFollow?user="+user_id)
    console.log($.parseJSON(data["responseText"]));
    return $.parseJSON(data["responseText"]);
}

function followClick(elem){
	var user_id = $('.profileBox').attr("id");
	var response = requestToggleFollow(user_id);
	var action = response["action"];
	if(action == "follow"){
		$('#followBt').html("seguindo");
		$(elem).attr("class", "following");
	}
	else{
		$('#followBt').html("seguir");
		$(elem).attr("class", "tofollow");
	}

}








// Inicializar o FACEBOOK
var isActive = false;

window.fbAsyncInit = function() 
{
	FB.init({
  		appId      : '195072584019284', // App ID
  		channelUrl : '',
  		status     : true, // check login status
  		cookie     : true, // enable cookies to allow the server to access the session
  		xfbml      : true  // parse XFBML
	});

	isActive = true;
};

(function(d)
{
	var js, id = 'facebook-jssdk', ref = d.getElementsByTagName('script')[0];
 
	if (d.getElementById(id)) {return;}
 	
 	js = d.createElement('script'); js.id = id; js.async = true;
 	js.src = "//connect.facebook.net/en_US/all.js";
	ref.parentNode.insertBefore(js, ref);
}(document)); 
	
function shareFacebook(id_post)
{
	var title = $('#' + id_post + ' .inner .head .title').text();

	if(isActive == true)
	{
		FB.getLoginStatus(function(response) 
		{
			if (response.status === 'connected') 
		  	{
			    var uid = response.authResponse.userID;
			    var accessToken = response.authResponse.accessToken;

			    post(title, id_post);
			} 
			else if (response.status === 'not_authorized') 
			{
			    
		  	}
		  	else 
		  	{
			    login();
			}
		});
	}
}

function login()
{
	if(isActive == true)
	{
	    FB.login(function(response) 
	    {
	       	if (response.authResponse) 
	       	{
	       		console.log('Login efectuado com sucesso!');
	        } 
	        else 
	        {
	        	console.log('Login nao foi efectuado com sucesso!');
	        }
	    },{scope: 'email,user_photos,user_videos'});
   }
}

function post(title, id_post)
{
	if(isActive == true)
	{
	    FB.ui(
	  	{
	  		// TEM QUE SE EXPERIMENTAR COM O PROJETO QUE ESTA GUARDADO NO FOODRIFIC.APPSPOT.COM
	    	method: 'feed',
	    	name: title,
	    	link: 'http://foodrific.appspot.com/post?id=' + id_post,
	    	picture: 'http://foodrific.appspot.com/api/postimage?id=' + id_post,
	    	description: 'Venha conhecer a publicação ' + title + ' da Foodrific! :)'
	  	},
	  	
	  	function(response) 
	  	{
	    	if (response && response.post_id) 
	    	{
	      		console.log('Publicacao publicada!!');
	    	} 
	    	else 
	    	{
	      		console.log('Publicacao nao publicada!!');
	    	}
	  	});
  	}
}


// Partilhar com o GOOGLE PLUS
function shareGooglePlus(id_post)
{
	// TEM QUE SE EXPERIMENTAR COM O PROJETO QUE ESTA GUARDADO NO FOODRIFIC.APPSPOT.COM
	var url = 'https://plus.google.com/u/0/share?url=http://foodrific.appspot.com/post?id='+ id_post +'&source=yt&hl=pt-PT&soc-platform=1&soc-app=130';
	
	window.open(url,'','width=450,height=300');
}



//Partilhar com o TWITTER
function shareTwitter(id_post)
{
	var title = $('#' + id_post + ' .inner .head .title').text();

	// TEM QUE SE EXPERIMENTAR COM O PROJETO QUE ESTA GUARDADO NO FOODRIFIC.APPSPOT.COM
	var url = 'https://twitter.com/intent/tweet?url=http://foodrific.appspot.com/post?id='+ id_post +'&text='+ title +'';
	window.open(url,'','width=450,height=300');
}

!function(d,s,id)
{
	var js,fjs=d.getElementsByTagName(s)[0];

	if(!d.getElementById(id))
	{
		js=d.createElement(s);
		js.id=id;
		js.src="https://platform.twitter.com/widgets.js";
		fjs.parentNode.insertBefore(js,fjs);
	}
}(document,"script","twitter-wjs");