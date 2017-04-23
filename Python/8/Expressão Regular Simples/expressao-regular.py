# coding: utf-8
# Expressão Regular
# Felipe Marinho (C) | 116110223 | <felipe.marinho@ccc.ufcg.edu.br>

def is_substring_expr(str1,str2):
	str1 = str.lower(str1)
	str2 = str.lower(str2).split("*")
	cont1 = 0
	cont2 = 0
	for i in range(len(str2[0])):
		if str1[i] == str2[0][i]:
			cont1 += 1
	for i in range(1,len(str2[1])+1):
		if str1[-i] == str2[1][-i]:
			cont2 += 1
	if cont1 == len(str2[0]) and cont2 == len(str2[1]):
		return True
	return False
