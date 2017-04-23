# coding: utf-8
# Desloca Elemento
# Felipe Marinho (C) | 116110223 | <felipe.marinho@ccc.ufcg.edu.br>

def desloca(lista, origem, destino):
	for i in range(origem,destino,1):
		lista[i], lista[i+1] = lista[i+1], lista[i]

l1 = [2,6,9,11,13,5]
desloca(l1, 2, 4)
assert l1 == [2,6,11,13,9,5]

l1 = [0,1,2,3,4,5,6]
desloca(l1, 4, 6)
assert l1 == [0,1,2,3,5,6,4]