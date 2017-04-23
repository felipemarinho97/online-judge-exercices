# coding: utf-8
# Sequencia de DNA
# Felipe Marinho (C) | 116110223 | <felipe.marinho@ccc.ufcg.edu.br>
import math

dna_1 = raw_input()
dna_2 = raw_input()
dna_iguais = 0

for i in range(len(dna_1)) :
	if dna_1[i] == dna_2[i] :
		dna_iguais += 1

tamanho = math.floor(len(dna_1)/2.0)

if dna_iguais > tamanho :
	print "sim"
else :
	print "nao"
