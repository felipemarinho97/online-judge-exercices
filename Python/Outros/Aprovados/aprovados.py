# coding: utf-8
# Aprovados
# Felipe Marinho (C) | 116110223 | <felipe.marinho@ccc.ufcg.edu.br>

numero_alunos = int(raw_input())
aprovados = 0

for i in range(numero_alunos) :
	media = raw_input()
	if media == "F" :
		aprovados += 0
	elif float(media) >= 5.0 :
		aprovados += 1
porcentagem = (100*aprovados)/numero_alunos
print "%i%% (%i/%i) de aprovados" % (porcentagem, aprovados, numero_alunos)
