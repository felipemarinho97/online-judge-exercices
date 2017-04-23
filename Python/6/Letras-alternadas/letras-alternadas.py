# coding: utf-8
# Letras Alternadas
# Felipe Marinho (C) | 116110223 | <felipe.marinho@ccc.ufcg.edu.br>

def letras_alternadas(string):
	letras_alternadas = ''
	for i in range(0,len(string),2):
		letras_alternadas += string[i]
	return letras_alternadas