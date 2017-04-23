# coding: utf-8
# Soma Polinômios
# Felipe Marinho (C) | 116110223 | <felipe.marinho@ccc.ufcg.edu.br>

def soma_polinomios(p1,p2):
	p1, p2 = p1[::-1], p2[::-1]
	soma = []
	if p1 > p2:
		maior = p1
		menor = p2
	elif p2 > p1:
		maior = p2
		menor = p1
	for i in range(len(menor)):
		soma.append(p1[i]+p2[i])
	for i in range(len(soma),len(maior),1):
		soma.append(maior[i])
	return soma[::-1]

p1 = [3, 4, -5]
p2 = [5, 0, 0, 0, 2, 0, -1]
assert soma_polinomios(p1, p2) == [5, 0, 0, 0, 5, 4, -6]