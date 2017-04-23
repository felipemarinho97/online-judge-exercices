# coding: utf-8
# Converte Matrícula
# Felipe Marinho (C) | 116110223 | <felipe.marinho@ccc.ufcg.edu.br>

matricula = raw_input()
matricula_nova = ''

for i in range(len(matricula)) :
	if i == 0 :
		matricula_nova += '1'
	elif i == 5 :
		matricula_nova += '0'
		matricula_nova += matricula[i]
	else :
		matricula_nova += matricula[i]
print matricula_nova
