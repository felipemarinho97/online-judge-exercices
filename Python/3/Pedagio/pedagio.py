# coding: utf-8
# Pedágio
# Felipe Marinho (C) | 116110223 | <felipe.marinho@ccc.ufcg.edu.br>

automovel = raw_input()


if automovel == "Motocicleta" :
	print "Valor a pagar: R$ %.2f." % 5.7
elif automovel == "Caminhão" :
	eixos = int(raw_input())
	print "Valor a pagar: R$ %.2f." % (9.6*eixos)
elif automovel == "Ônibus" :
	eixos = int(raw_input())
	print "Valor a pagar: R$ %.2f." % (11.4*eixos)
elif automovel == "Automóvel utilitário" :
	print "Valor a pagar: R$ %.2f." % 11.4
else :
	print "Veículo não cadastrado."
