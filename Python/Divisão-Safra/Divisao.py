# coding: utf-8
# Divisão Safra
# Felipe Marinho (C) | 116110223

soja = float(raw_input())
clientes_atacado = int(raw_input())
clientes_varejo = int(raw_input())

print "Clientes no atacado = %ikg cada." % (soja / clientes_atacado)
print "Clientes no varejo = %.2fkg cada." % ((soja % clientes_atacado) / clientes_varejo)
