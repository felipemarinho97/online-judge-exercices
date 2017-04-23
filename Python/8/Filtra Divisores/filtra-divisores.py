# coding: utf-8
# Filtra Divisores
# Felipe Marinho (C) | 116110223 | <felipe.marinho@ccc.ufcg.edu.br>

def soma_algarismos(num):
	soma = 0
	for e in str(num):
		soma += int(e)
	return soma

def filtra_divisores(lista):
	for i in range(len(lista)-1,-1,-1):
		if lista[i] % soma_algarismos(lista[i]) != 0:
			lista.pop(i)

lista1 = [333, 121, 81]
assert filtra_divisores(lista1) == None
assert lista1 == [333,81]