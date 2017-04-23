# coding: utf-8
# Sequencia de DNA
# Felipe Marinho (C) | 116110223 | <felipe.marinho@ccc.ufcg.edu.br>

dna_1 = raw_input()
dna_2 = raw_input()
dna_iguais = 0  # Em que dna_iguais é a quantidade de sequências DNA iguais
maior_sequincia = 0

for i in range(len(dna_1)) :
	if dna_1[i] == dna_2[i] :
		dna_iguais += 1
	elif dna_1[i] != dna_2[i] and dna_iguais > maior_sequincia :
		maior_sequincia = dna_iguais
		dna_iguais = 0
	elif dna_1[i] != dna_2[i]  :
		dna_iguais = 0
if dna_iguais >= len(dna_1)/2.0 or maior_sequincia >= len(dna_1)/2.0 :
	print "sim"
else :
	print "nao"
