/**
 * Created by juniorlima on 15/06/2015.
 * http://codigofonte.uol.com.br/codigos/mascara-de-telefone-de-9-digitos-com-ddd-em-javascript
 */

/* Máscaras ER */
function mascara(o,f){
    v_obj=o
    v_fun=f
    setTimeout("execmascara()",1)
}
function execmascara(){
    v_obj.value=v_fun(v_obj.value)
}
function mtel(v){
    v=v.replace(/\D/g,"");             //Remove tudo o que não é dígito
    v=v.replace(/^(\d{2})(\d)/g,"($1) $2"); //Coloca parênteses em volta dos dois primeiros dígitos
    v=v.replace(/(\d)(\d{4})$/,"$1-$2");    //Coloca hífen entre o quarto e o quinto dígitos
    return v;
}
function id( el ){
	return document.getElementById( el );
}
window.onload = function(){
	id('id_telefone').onkeypress = function(){
		mascara( this, mtel );
	};
    id('id_telefone_adc').onkeypress = function(){
		mascara( this, mtel );
	};
    id('id_telefone_caseiro').onkeypress = function(){
		mascara( this, mtel );
	}
}