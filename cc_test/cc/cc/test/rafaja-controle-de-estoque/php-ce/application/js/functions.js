	function Ajax(remetente,destinatario,tabela){
		
	 
      $('select[@name='+destinatario+']').html('<option value="sda">Aguarde....</option>');
    
      
        $.ajax({
        	type: 'POST',
        	url: 'application/model/Ajax.php?tabela='+tabela+'&remetente='+remetente,
        	data: 'where='+document.getElementById(remetente).value,
        	//beforeSend: function(){ alert('enviando');},
        	success: 
        		function(resposta){  
        			$('select[@name='+destinatario+']').html(resposta);
   
        				}
  
       
  
        } );
  
      
		
	}

