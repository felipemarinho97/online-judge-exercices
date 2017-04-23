# coding: utf-8
# Verifica Esteira
# Felipe Marinho (C) | 116110223 | <felipe.marinho@ccc.ufcg.edu.br>

def verifica_esteira(l1,l2):
	i = -1
	for e in l2:
		chave = False
		for k in range(len(l1)):
			if l1[k] == e and k > i:
				chave = True
				i = k
				break
		if not chave:
			return False
	return True

# l1 = [2,1,3,4]
# l2 = [2]
# print verifica_esteira(l1,l2)

l1 = [1,3,4]
l2 = [4,1]
assert not verifica_esteira(l1,l2)
assert l1 == [1,3,4]


