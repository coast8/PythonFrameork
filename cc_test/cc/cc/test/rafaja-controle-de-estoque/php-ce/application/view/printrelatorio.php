<?php
$datainicial=$_GET['datainicial'];
$datafinal=$_GET['datafinal'];
$acao=$_GET['acao'];
$tabela=$_GET['tabela'];
include '../controler/Form.php';
include '../controler/Relatorios.php';
include '../controler/DB.php';
header("Content-Disposition: attachment; filename=$tabela.html ;"); 
echo '<html>';
echo '<body>';
echo '<style type="text/css">
body{
	margin:0px;
	padding:0px;
	font-family:verdana,arial;
	font-size: 12px;
	margin-top:60px;
}
.img {
	align:middle;
	border:0px;
}
.img a{
	border:1px;
	text-decorarion: none;
}

td{
	background-color:#f6f6f6;
	font-size:12px;
	width:150px;
}
a {
	color: #333;
	text-decoration:none;
}

td.header {
	font-weight:bold;
}

#Full{
	border:1px solid #333;
	width:70%;
	margin: 1em auto;
	height:90%;
	
}

#Menu{
	
	
	background-color:#324143;
	width:100%;
	height:25px;
	text-align:center;
	color: white;
	
		
}

#Logo {
	
	text-align:center;
	width:100%;
	height: 50px;
	padding-top:10px;
}
#Content {
	width:80%;
	margin-top:60px;
	margin: 1em auto;
	height:70%;
	overflow:auto;
}

#Alerta{
	width: 350px;
	height: 200px;
	margin: 1em auto;
	margin-top:50px;
	overflow:auto;
	text-align:center;
	
		}
	
.txt_bold{
font-weight:bold;

}</style>';


switch ($acao){
	case 'Visualizar':
	$relatorio=new Relatorio($tabela);
	$relatorio->Visualizar();
	break;
	
	case 'Entrada':
	$relatorio=new Relatorio('entrada');
	$relatorio->Entrada($datainicial,$datafinal,'s');
	break;
	
	case 'Saida':
$relatorio=new Relatorio('saida');
	$relatorio->Entrada($datainicial,$datafinal,'s');
	break;
	
		
	
	
	
}

echo '</body></html>';
?>