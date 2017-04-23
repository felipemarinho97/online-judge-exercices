# coding: utf-8
# Resumo Compras
# Felipe Marinho (C) | 116110223 | <felipe.marinho@ccc.ufcg.edu.br>

compras = []

while True:
	precos = raw_input()
	if precos == "fim":
		break
	else:
	        compras.append(float(precos))

