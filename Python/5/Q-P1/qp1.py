# coding: utf-8
# Questões para P1
# Felipe Marinho (C) | 116110223 | <felipe.marinho@ccc.ufcg.edu.br>

dados = []
questao_por_professor = 0
entrada = ''
questoes = ''
total = 0

while True:
	entrada = raw_input()
	if entrada == '**': break
	while True:
		questoes = raw_input()
		if questoes == '*': break
		questao_por_professor += int(questoes)
		total += int(questoes)
	dados.append(entrada)
	dados.append(questao_por_professor)
	questao_por_professor = 0

print "Relatório de novas questões:\n"
for i in range(len(dados)):
	if i % 2 == 1:
		print "%s: %s" % (dados[i-1], dados[i])
print """---
Total de novas questões: %i""" % total