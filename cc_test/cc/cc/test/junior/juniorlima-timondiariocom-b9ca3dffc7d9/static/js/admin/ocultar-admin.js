jQuery(function($) {
    $("#evento_noticia_set-group").hide();

    $("#video_noticia_set-group").hide();

	$("#id_categoria_nome").change(function(){
		var value = $(this).val();
        if(value == ''){
			$("#evento_noticia_set-group").hide();
			$("#video_noticia_set-group").hide();
		}
		if(value == 3){
			$("#evento_noticia_set-group").show();
            $("#video_noticia_set-group").hide();
		}
        if(value == 7){
			$("#video_noticia_set-group").show();
            $("#evento_noticia_set-group").hide();
		}
	});

    $("#s2id_id_evento_noticia_set-0-local").change(function(){
        $("#control-group").show();
    });
});
