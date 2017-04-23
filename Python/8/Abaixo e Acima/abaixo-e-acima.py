# coding: utf-8
# Abaixo e Acima
# Felipe Marinho (C) | 116110223 | <felipe.marinho@ccc.ufcg.edu.br>

def organiza_por_media(lista):
	organiza = []
	maior = []
	menor = []
	soma = 0
	for e in lista:
		soma += e
	try:
		media = soma/float(len(lista))
	except:
		pass
	for i in range(len(lista)):
		if lista[i] <= media:
			menor.append(lista[i])
		else:
			maior.append(lista[i])
	for i in range(len(menor)):
		organiza.append(menor[i])
	for i in range(len(igual)):
		organiza.append(igual[i])
	for i in range(len(maior)):
		organiza.append(maior[i])
	return organiza

# p1 = [1.0,8,100,0,0]
# print organiza_por_media(p1)