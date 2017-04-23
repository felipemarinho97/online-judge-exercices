# coding: utf-8
# Transporte
# Felipe Marinho (C) | 116110223 | <felipe.marinho@ccc.ufcg.edu.br>

import math

pessoas = int(raw_input())
dinheiro = float(raw_input())

# Custo de cada transporte dado em reais
custo_tav = 100.0 * pessoas
custo_onibus = 22.0 * pessoas
custo_taxi = math.ceil(pessoas/4.0) * 200.0

if dinheiro >= custo_tav :
	print "TAV. R$ %.2f" % custo_tav
elif dinheiro >= custo_taxi :
	print "Táxi. R$ %.2f" % custo_taxi
elif dinheiro >= custo_onibus :
	print "Ônibus. R$ %.2f" % custo_onibus
else :
	print "Não é possível realizar a viagem."
