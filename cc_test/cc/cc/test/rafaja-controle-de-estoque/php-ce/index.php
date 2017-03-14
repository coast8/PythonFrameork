<?php 
$url=$_GET['url'];
$url=(empty($url))?"index":$url;


include 'application/controler/Produtos.php';
include 'application/controler/Retirantes.php';
include 'application/controler/Fornecedores.php';
include 'application/controler/Form.php';
include 'application/controler/Relatorios.php';
include 'application/controler/DB.php';

?>
<html>
<head>
<title>SISTEMA DE ESTOQUE 1.0</title>
<style type="text/css">
@import url("styles/index.css");
@import url("styles/menu.css");
</style>
<script type="text/javascript" src="application/js/jquery.min.js"></script>
<script type="text/javascript" src="application/js/menu.js"></script>
<script type="text/javascript" src="application/js/functions.js"></script>
</head>
<body>
<div id="Full">
<div id="Logo">SISTEMA DE CONTROLE DE ESTOQUE E ALMOXARIFADO</div>
<div id="Menu">
	<ul id="jsddm">
	<li><a href="#">Produtos</a>
		<ul>
			<li><a href="index.php?url=produto&acao=formcadastrocategoria">Cadastrar Categoria</a></li>
			<li><a href="index.php?url=produto&acao=formcadastro">Cadastrar Produtos</a></li>
			<li><a href="index.php?url=produto&acao=listar">Listar Produtos</a></li>
		</ul>
	</li>
	<li><a href="#">Estoque</a>
		<ul>
			<li><a href="index.php?url=estoque&acao=formcadastroentrada">Entrada de Material</a></li>
			<li><a href="index.php?url=estoque&acao=formcadastrosaida">Saida de Material</a></li>
		</ul>
	</li>
	<li><a href="#">Fornecedores</a>
		<ul>
			<li><a href="index.php?url=fornecedor&acao=formcadastro">Cadastrar Fornecedor</a></li>
			<li><a href="index.php?url=fornecedor&acao=listar">Listar Fornecedores</a></li>
		</ul>
	</li>
	<li><a href="#">Retirantes</a>
		<ul>
			<li><a href="index.php?url=retirante&acao=formcadastro">Cadastrar Retirante</a></li>
			<li><a href="index.php?url=retirante&acao=listar">Listar Retirantes</a></li>
		</ul>
	</li>
	<li><a href="#">Relatórios</a>
		<ul>
			<li><a href="index.php?url=relatorio&acao=produto">Produtos</a></li>
			<li><a href="index.php?url=relatorio&acao=fornecedor">Fornecedores</a></li>
			<li><a href="index.php?url=relatorio&acao=retirante">Retirantes</a></li>
			<li><a href="index.php?url=relatorio&acao=entrada">Entrada</a></li>
			<li><a href="index.php?url=relatorio&acao=saida">Saida</a></li>
		</ul>
	</li>
	
		<li><a href="#">Impressão</a>
		<ul>
			<li><a href="index.php?url=relatorio&acao=produto">Produtos</a></li>
			<li><a href="index.php?url=relatorio&acao=fornecedor">Fornecedores</a></li>
			<li><a href="index.php?url=relatorio&acao=retirante">Retirantes</a></li>
			<li><a href="index.php?url=relatorio&acao=entrada">Entrada</a></li>
			<li><a href="index.php?url=relatorio&acao=saida">Saida</a></li>
		</ul>
	</li>
	
</ul>
</div>
<div id="Content"><?php include 'application/view/'.$url.'.phtml'; ?></div>
</div>





</body>
</html>
