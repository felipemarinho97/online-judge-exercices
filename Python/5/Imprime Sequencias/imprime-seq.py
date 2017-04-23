# coding: utf-8
# Imprime Sequências
# Felipe Marinho (C) | 116110223 | <felipe.marinho@ccc.ufcg.edu.br>

import string

numero = float(raw_input())
sequencias = []

while True:
	sequencia = raw_input()
	if sequencia == "fim":
		break
	else:
		sequencias.append(sequencia.split())
for i in range(len(sequencias)):
	maiores = 0
	for j in range(len(sequencias[i])):
		if int(sequencias[i][j]) > numero:
			maiores += 1
		if maiores > (len(sequencias[i])/2):
			print "sequencia %i:" % (i+1) ,string.join(sequencias[i])
			break
			
