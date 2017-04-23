# coding: utf-8
# Inverte Triplas
# Felipe Marinho (C) | 116110223 | <felipe.marinho@ccc.ufcg.edu.br>

def inverte3a3(s):
	inverte3a3 = ''
	for i in range(len(s)-3,-3,-3):
		thrid = ''
		for j in range(3):
			thrid += s[i+j]
		inverte3a3 += thrid
	return inverte3a3
