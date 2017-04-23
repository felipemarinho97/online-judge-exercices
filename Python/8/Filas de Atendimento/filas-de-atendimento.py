# coding: utf-8
# Filas de Atendimento
# Felipe Marinho (C) | 116110223 | <felipe.marinho@ccc.ufcg.edu.br>

def filas_de_atendimento(fila_unica,n):
	filas_de_atendimento = []
	for i in range(n):
		filas_de_atendimento.append([])
	j = 0
	for i in range(len(fila_unica)):
		filas_de_atendimento[j].append(fila_unica[i])
		if j < n-1:
			j += 1
		elif j >= n-1:
			j = 0
	return filas_de_atendimento

