# coding: utf-8
# Calculadora de Médias
# Felipe Marinho (C) | 116110223 | <felipe.marinho@ccc.ufcg.edu.br>

def media_aritimetica(numeros):
	numeros = numeros.split()
	soma = 0
	for i in range(len(numeros)):
		soma += float(numeros[i])
	media = soma/float(len(numeros))
	return media

def media_geometrica(numeros):
	numeros = numeros.split()
	n = len(numeros)
	produto = float(numeros[0])
	for i in range(1,n,1):
		produto *= float(numeros[i])
	media = produto**(1/float(n))
	return media

def media_harmonica(numeros):
	numeros = numeros.split()
	n = len(numeros)
	soma = 0
	for i in range(n):
		soma += 1/float(numeros[i])
	media = n/soma
	return media

medias = []

while True:
	metodo = raw_input().split()
	if metodo[0] == "Q":
		break
	sequencia = raw_input()
	for i in range(len(metodo)):
		if metodo[i] == "MA":
			medias.append("Média Aritmética")
			medias.append(media_aritimetica(sequencia))
		elif metodo[i] == "MG":
			medias.append("Média Geométrica")
			medias.append(media_geometrica(sequencia))
		elif metodo[i] == "MH":
			medias.append("Média Harmônica")
			medias.append(media_harmonica(sequencia))
	medias.append("-")

for i in range(len(medias)):
	if medias[i] == "-":
		print "----"
	elif type(medias[i]) == float:
		print "%s: %.4f" % (medias[i-1],medias[i])