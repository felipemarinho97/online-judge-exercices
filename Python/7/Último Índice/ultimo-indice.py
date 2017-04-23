# coding: utf-8
# Último Índice
# Felipe Marinho (C) | 116110223 | <felipe.marinho@ccc.ufcg.edu.br>

def ultimo_indice(num,lista):
	indice = -1
	for i in range(len(lista)):
		if lista[i] == num:
			indice = i
	return indice