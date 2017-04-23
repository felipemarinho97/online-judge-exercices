# coding: utf-8
# Triângulos
# Felipe Marinho (C) | 116110223 | <felipe.marinho@ccc.ufcg.edu.br>

def conversor_inteiro(lista):
	for i in range(len(lista)):
		lista[i] = float(lista[i])
	return lista

triangulos = []

while True:
	entrada = raw_input()
	if entrada == "fim": break
	triangulos.append(entrada)

equilateros = 0
escalenos = 0
isoceles = 0
validos = 0

for i in range(len(triangulos)):
	valores = conversor_inteiro(triangulos[i].split())
	if valores[0] <= (valores[1] + valores[2]) and valores[1] <= (valores[0] + valores[2]) and valores[2] <= (valores[1] + valores[0]):
		validos += 1
		if valores[0] == valores[1] and valores[0] == valores[2]:
			equilateros += 1 
		elif valores[0] == valores[1] and valores[0] == valores[2] and valores[1] == valores[2]:
			isoceles += 1
		else:
			escalenos += 1

invalidos = len(triangulos) - validos

if equilateros > 0: print "equilateros: %i" % equilateros
if escalenos > 0: print "escalenos: %i" % escalenos
if isoceles > 0: print "isoceles: %i" % isoceles
if invalidos > 0: print "nao triangulos: %i" % invalidos
