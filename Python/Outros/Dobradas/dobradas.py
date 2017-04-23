# coding: utf-8
# Letras Dobradas
# Felipe Marinho (C) | 116110223 | <felipe.marinho@ccc.ufcg.edu.br>

numero_de_palavras = int(raw_input())
palavras = []
palavras_dobradas = []

for i in range(numero_de_palavras) :
	palavra = raw_input()
	palavras.append(palavra)
	for j in range(len(palavra)) :
		if j > 0 and palavra[j] == palavra[(j-1)] :
			palavras_dobradas.append(palavra)
			palavras.remove(palavra)
			break
			
print "%i palavra(s) com letras dobradas:" % len(palavras_dobradas)
for i in range(len(palavras_dobradas)) :
	print palavras_dobradas[i]
print "---"
print "%i palavra(s) sem letras dobradas:" % len(palavras)
for i in range(len(palavras)) :
	print palavras[i]

