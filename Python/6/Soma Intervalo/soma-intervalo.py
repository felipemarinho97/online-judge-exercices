# coding: utf-8
# Soma Intervalo
# Felipe Marinho (C) | 116110223 | <felipe.marinho@ccc.ufcg.edu.br>

def soma_intervalo(a,b):
	somaintervalo = 0
	for i in range(a,b+1,1):
		somaintervalo += i
	return somaintervalo

assert soma_intervalo(5,15) == 110
assert soma_intervalo(10,10) == 10