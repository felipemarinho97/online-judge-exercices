# coding: utf-8
# Câmbio
# Felipe Marinho (C) | 116110223 | <felipe.marinho@ccc.ufcg.edu.br>

entradas = []
real = 1
peso = 2.58
dolar = 0.49
euro = 0.38

while True:
	entrada = raw_input()
	if entrada == "fim": 
		break
	entradas.append(entrada)

for i in range(len(entradas)):
	lista_manipulavel = entradas[i].split()
	if lista_manipulavel[-1] == "$":
		cambio = float(lista_manipulavel[1])*peso
	elif lista_manipulavel[-1] == "U$":
		cambio = float(lista_manipulavel[1])*dolar
	elif lista_manipulavel[-1] == "€":
		cambio = float(lista_manipulavel[1])*euro
	print "R$ %.2f = %s %.2f" % (float(lista_manipulavel[1]),lista_manipulavel[-1],cambio)

