# coding: utf-8
# Acima de
# Felipe Marinho (C) | 116110223 | <felipe.marinho@ccc.ufcg.edu.br>

def acima_de(N,L):
	acima_de = []
	for i in range(len(L)):
		if L[i] > N:
			acima_de.append(i)
	return acima_de