# coding: utf-8
# Quantos Comeram?
# Felipe Marinho (C) | 116110223 | <felipe.marinho@ccc.ufcg.edu.br>

def quantos_comeram(n,fila):
	feijoadas = n
	quantos_comeram = 0
	for i in range(len(fila)):
		feijoadas -= fila[i]
		if feijoadas == 0:
			return quantos_comeram+fila[i]
		elif feijoadas < 0:
			return quantos_comeram
		quantos_comeram += fila[i]

assert quantos_comeram(10, [10, 10]) == 10
assert quantos_comeram(12, [10, 10]) == 10
assert quantos_comeram(2, [10, 10]) == 0
assert quantos_comeram(5, [2, 3, 5]) == 5