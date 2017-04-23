# coding: utf-8
# Retorna Maior e Menor Número
# Felipe Marinho (C) | 116110223 | <felipe.marinho@ccc.ufcg.edu.br>

def retorna_maior_menor(lista):
	maior_menor = [lista[0], lista[0]]
	for i in range(len(lista)):
		if maior_menor[0] < lista[i]:
			maior_menor[0] = lista[i]
		if maior_menor[1] > lista[i]:
			maior_menor[1] = lista[i]
	return maior_menor