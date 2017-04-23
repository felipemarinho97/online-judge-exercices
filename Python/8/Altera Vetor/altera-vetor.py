# coding: utf-8
# Altera Vetor
# Felipe Marinho (C) | 116110223 | <felipe.marinho@ccc.ufcg.edu.br>

def altera_vetor_por_escalar(vetor, escalar):
	for i in range(len(vetor)):
		vetor.append(vetor[0]*escalar)
		vetor.pop(0)

vetor_1 = [1, 2, 3]
assert altera_vetor_por_escalar(vetor_1, -1) == None
assert vetor_1 == [-1, -2, -3]
assert altera_vetor_por_escalar(vetor_1, 2) == None
assert vetor_1 == [-2, -4, -6]
