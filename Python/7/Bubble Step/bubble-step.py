# coding: utf-8
# Bubble Step
# Felipe Marinho (C) | 116110223 | <felipe.marinho@ccc.ufcg.edu.br>

def bubblestep(lista):
	for i in range(len(lista)-1):
		if int(lista[i]) >= int(lista[i+1]):
			lista[i], lista[i+1] = lista[i+1], lista[i]

def meu_join(lista):
	string = ''
	if len(lista) == 0:
		return string
	for i in range(len(lista)-1):
		string += str(lista[i]) + " "
	string += str(lista[-1])
	return string

resultados = []

while True:
	entrada = raw_input()
	if entrada == "fim": break
	entrada = entrada.split()
	bubblestep(entrada)
	resultados.append(meu_join(entrada))

for e in resultados:
	print e