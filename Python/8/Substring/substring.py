# coding: utf-8
# Substring
# Felipe Marinho (C) | 116110223 | <felipe.marinho@ccc.ufcg.edu.br>

def is_substring(str1,str2):
	for i in range(len(str1)):
		chave = True
		cont = 0
		if str2[0] == str1[i]:
			for j in range(len(str2)):
				if str1[i+j] == str2[j]:
					chave == True
					cont += 1
				else:
					chave = False
				if not chave:
					break
		if cont == len(str2):
			return True
	return False

assert is_substring('boiada','oi')
assert not is_substring('casorio', 'casa')
