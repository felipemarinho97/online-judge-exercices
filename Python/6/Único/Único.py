# coding: utf-8
# Único
# Felipe Marinho (C) | 116110223 | <felipe.marinho@ccc.ufcg.edu.br>

def unico(string):
	unico = ""
	if len(string) < 1:
		return unico
	for i in range(len(string)-1):
		if string[i] == string[i+1]:
			None
		else:
			unico += string[i]
	unico += string[-1]
	return unico

assert unico("aa***xxxzzb+") == "a*xzb+"
assert unico("") == ""
