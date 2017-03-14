<?php
include '../controler/DB.php';
$tabela=$_GET['tabela'];
$remetente=$_GET['remetente'];
$where=$_POST['where'];
$DB=new DB();

$rows=$DB->ExecutaQuery("Select * from $tabela where $remetente=$where");

while($row=mysql_fetch_array($rows)){
	
	
	echo '<option value="'.$row[id].'">'.$row[nome].'</option>';
	
}



?>