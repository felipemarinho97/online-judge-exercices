# coding: utf-8
# União de Listas
# Felipe Marinho (C) | 116110223 | <felipe.marinho@ccc.ufcg.edu.br>

def meu_in(k,lista):
	for e in lista:
		if e == k:
			return True
	return False

def remove_repetidos(l):
	for e in l:
		cont = 0
		for j in l:
			if e == j:
				cont += 1
				if cont > 1:
					l.remove(j)
	return l


def uniao_listas(l1,l2):
	for e in remove_repetidos(l2):
		if not (meu_in(e,remove_repetidos(l1))):
			l1.append(e)

# l1 = [2,1,1,1,3,4]
# l2 = [2,2]
# print remove_repetidos(l1)
# uniao_listas(l1,l2)
# print l1