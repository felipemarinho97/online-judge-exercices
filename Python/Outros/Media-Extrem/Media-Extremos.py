# coding: utf-8
# Média dos Extremos
# Felipe Marinho (C) | 116110223 | <felipe.marinho@ccc.ufcg.edu.br>

elementos = int(raw_input())
lista = []
acima_da_media = 0
abaixo_da_media = 0

for i in range(elementos) :
	elemento = int(raw_input())
	if i == 0 :
		maior = elemento
		menor = elemento
	lista.append(elemento)
	if lista[i] > maior :
		maior = lista[i]
	elif lista[i] < menor :
		menor = lista[i]
media = (maior + menor)/2.0

for i in range(elementos) :
	if lista[i] > media :
		acima_da_media += 1
	elif lista[i] < media :
		abaixo_da_media += 1
print """Menor número: %i
Maior número: %i
Média dos extremos: %.2f
%i número(s) abaixo da média
%i número(s) acima da média""" % (menor, maior, media, abaixo_da_media, acima_da_media)
