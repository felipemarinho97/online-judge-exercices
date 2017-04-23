# coding: utf-8
# Pivot
# Felipe Marinho (C) | 116110223 | <felipe.marinho@ccc.ufcg.edu.br>

def pivot(numeros):
	ultimo_dos_numeros = 1
	for i in range(1,len(numeros)): # Ordena os menores à esquerda e os maiores à direita
		if numeros[i] < numeros[0]:
			for j in range(i,ultimo_dos_numeros,-1):
				numeros[j], numeros[j-1] = numeros[j-1], numeros[j]
			ultimo_dos_numeros += 1
	for i in range(1,len(numeros)): # Para o caso de ter valores iguais ao pivot
		if numeros[i] == numeros[0]:
			if i > ultimo_dos_numeros:
				for i in range(i,ultimo_dos_numeros,-1):
					numeros[i], numeros[i-1] = numeros[i-1], numeros[i]
			else:
				for i in range(i,ultimo_dos_numeros):
					numeros[i], numeros[i+1] = numeros[i+1], numeros[i]
	for i in range(0,ultimo_dos_numeros-1): # Coloca o pivot na sua posição final
		numeros[i], numeros[i+1] = numeros[i+1], numeros[i]