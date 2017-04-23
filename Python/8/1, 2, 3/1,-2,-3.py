# coding: utf-8
# 1, 2, 3
# Felipe Marinho (C) | 116110223 | <felipe.marinho@ccc.ufcg.edu.br>

def tem123plus(l):
	key1 = False
	key2 = False
	for i in range(len(l)):
		if l[i] == 1 and not key1:
			key1 = True
			indice = i
		if l[i] == 2 and key1:
			key2 = True
		if l[i] == 3 and key2:
			return indice
	return -1

assert tem123plus([3,2,1,2,3]) == 2
assert tem123plus([4,1,1,1,4,2,3]) == 1
assert tem123plus([1,2,2,3]) == 0
assert tem123plus([1,2,2,4]) == -1