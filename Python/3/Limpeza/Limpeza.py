# coding: utf-8
# Limpeza
# Felipe Marinho (C) | 116110223 | <felipe.marinho@ccc.ufcg.edu.br>

servico = int(raw_input())

if servico == 1 :
	tamanho_m3 = float(raw_input())
	print "R$ %i,00" % (tamanho_m3 * 80)
	if (tamanho_m3 * 80) >= 200 :
		print "Brinde!"
elif servico == 2 :
	tamanho_m3 = float(raw_input())
	print "R$ %i,00" % (tamanho_m3 * 50)
	if (tamanho_m3 * 50) >= 200 :
		print "Brinde!"
elif servico == 3 :
	print "R$ %i,00" % 50
