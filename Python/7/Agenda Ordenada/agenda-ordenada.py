# coding: utf-8
# Agenda Ordenada
# Felipe Marinho (C) | 116110223 | <felipe.marinho@ccc.ufcg.edu.br>

def insere_ordenado(nome,lista):
	lista.append(nome)
	for i in range(len(lista)-1,0,-1):
		if lista[i] < lista[i-1]:
			lista[i], lista[i-1] = lista[i-1], lista[i]

nomes = []

while True:
	entrada = raw_input()
	if entrada == "####":
		break
	insere_ordenado(entrada,nomes)
	for e in nomes:
		if e == entrada:
			print "* %s" % e
		else:
			print e
	print "----"