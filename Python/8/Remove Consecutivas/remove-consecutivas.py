# coding: utf-8
# Remove Consecutivas
# Felipe Marinho (C) | 116110223 | <felipe.marinho@ccc.ufcg.edu.br>

def remove_consecutivas(lista):
	for k in range(len(lista)-1,-1,-1):
		for i in range(len(lista[k])-1):
			if lista[k][i].lower() == lista[k][i+1].lower():
				lista.pop(k)
				break