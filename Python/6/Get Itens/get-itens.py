# coding: utf-8
# Get Itens
# Felipe Marinho (C) | 116110223 | <felipe.marinho@ccc.ufcg.edu.br>

def get_items(valores,indices):
	itens = []
	for i in indices:
		if i < len(valores):
			itens.append(valores[i])
		else:
			itens.append(None)
	return itens