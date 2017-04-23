# coding: utf-8
# Paridade
# Felipe Marinho (C) | 116110223 | <felipe.marinho@ccc.ufcg.edu.br>

def paridade(numero):
	cont = 0
	for i in range(len(numero)-1):
		if numero[i] == '1':
			cont += 1
	if cont % 2 == 0 and numero[-1] == '0':
		return True
	elif cont % 2 == 1 and numero[-1] == '1':
		return True
	else:
		return False

while True:
	numero = raw_input()
	if paridade(numero) == False:
		print "ERRO"
		break
