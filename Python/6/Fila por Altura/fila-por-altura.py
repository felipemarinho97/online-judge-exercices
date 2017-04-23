# coding: utf-8
# Fila por Altura
# Felipe Marinho (C) | 116110223 | <felipe.marinho@ccc.ufcg.edu.br>

def insere_na_fila(fila, nome, altura):
	fila.append((nome, altura))
	for i in range(len(fila)-1,0,-1):
		if fila[i][1] < fila[i-1][1]:
			fila[i], fila[i-1] = fila[i-1], fila[i]

fila = [("maria", 1.05), ("joao", 1.09), ("ana", 1.16)]
insere_na_fila(fila, "jose", 1.12)
assert fila == [("maria", 1.05), ("joao", 1.09), ("jose", 1.12), ("ana", 1.16)]

fila = [("andre", 1.15), ("daniel", 1.19), ("carlos", 1.26)]
insere_na_fila(fila, "marcos", 1.17)
assert fila == [("andre", 1.15), ("marcos", 1.17), ("daniel", 1.19), ("carlos", 1.26)], fila
