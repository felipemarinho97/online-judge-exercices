# coding: utf-8
# Gratificação Natalina
# Felipe Marinho (C) | 116110223 | <felipe.marinho@ccc.ufcg.edu.br>

codigo_cargo = int(raw_input())

if codigo_cargo == 1 :
	print "Deverá receber em dezembro R$ %.2f." % 25000.00
elif codigo_cargo == 2 :
	print "Deverá receber em dezembro R$ %.2f." % 15000.00
elif codigo_cargo == 3 :
	faltas = int(raw_input())
	if faltas == 0 :
		gratificacao = 500
	else :
		gratificacao = (235 - faltas) * 2
	print "Valor da gratificação R$ %.2f." % gratificacao
	print "Deverá receber em dezembro R$ %.2f." % (8000+gratificacao)
elif codigo_cargo == 4 :
	faltas = int(raw_input())
	if faltas == 0 :
		gratificacao = 300
	else :
		gratificacao = (235 - faltas) * 1
	print "Valor da gratificação R$ %.2f." % gratificacao
	print "Deverá receber em dezembro R$ %.2f." % (5000+gratificacao)
elif codigo_cargo == 5 :
	faltas = int(raw_input())
	if faltas == 0 :
		gratificacao = 200
	else :
		gratificacao = (235 - faltas) * 0.7
	print "Valor da gratificação R$ %.2f." % gratificacao
	print "Deverá receber em dezembro R$ %.2f." % (2800+gratificacao)
