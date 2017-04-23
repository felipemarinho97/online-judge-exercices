# coding: utf-8
# Reduções
# Felipe Marinho (C) | 116110223 | <felipe.marinho@ccc.ufcg.edu.br>

def reducoes(seq):
	reducoes = []
	for i in range(len(seq)-1):
		valor = seq[i] - seq[i+1]
		if valor >= 0:
			reducoes.append(valor)
		else:
			reducoes.append(0)
	return reducoes

assert reducoes([4, 2, 0, 6, 3, 4]) == [2, 2, 0, 3, 0]
assert reducoes([3, 0, 3, 6, 1]) == [3, 0, 0, 5]