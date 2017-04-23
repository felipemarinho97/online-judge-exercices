# coding: utf-8
# Soma e Diminui Vizinhos
# Felipe Marinho (C) | 116110223 | <felipe.marinho@ccc.ufcg.edu.br>

def soma_diminui_vizinhos(lista):
	if lista == []:
		return 0
	soma_diminui = lista[0]
	for i in range(1,len(lista),2):
		soma_diminui += lista[i]
		if i+1 > len(lista)-1:
			break
		soma_diminui -= lista[i+1]
	return soma_diminui