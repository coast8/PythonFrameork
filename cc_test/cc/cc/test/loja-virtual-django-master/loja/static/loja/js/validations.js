function iniciar_valores () {
	document.getElementById("valor_minimo").value = 0
	document.getElementById("valor_maximo").value = 0
}

function validar_valores_de_busca () {
	valor_minimo = document.getElementById("valor_minimo").value
	valor_maximo = document.getElementById("valor_maximo").value

	if (valor_minimo == "") document.getElementById("valor_minimo").value = 0
	if (valor_maximo == "") document.getElementById("valor_maximo").value = 1000

	if (valor_minimo > valor_maximo) {
		auxiliar = valor_minimo
		document.getElementById("valor_minimo").value = valor_maximo
		document.getElementById("valor_maximo").value = auxiliar
	}
}
