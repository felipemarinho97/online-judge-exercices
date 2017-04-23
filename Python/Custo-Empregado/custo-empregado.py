# coding: utf-8
# Limpeza
# Felipe Marinho (C) | 116110223 | <felipe.marinho@ccc.ufcg.edu.br>

# Entrada
salario_base = float(raw_input())
dias_trabalhados = int(raw_input())
custo_transporte_dia = float(raw_input())

# Custo Empregador
if custo_transporte_dia*dias_trabalhados > salario_base*0.06 :
	transporte_empregador = (custo_transporte_dia*dias_trabalhados) - (salario_base*0.06)
else :
	transporte_empregador = 0
fgts_empregador = salario_base*0.08
inss_empregador = salario_base*0.12

# Custo Empregado
if custo_transporte_dia*dias_trabalhados >= salario_base*0.06 :
	transporte_empregado = salario_base*0.06
else :
	transporte_empregado = 0
if salario_base > 0 and salario_base <= 1317.07 :
	inss_empregado = salario_base*0.08
elif salario_base > 1317.08 and salario_base <= 2195.12 :
	inss_empregado = salario_base*0.09
elif salario_base > 2195.13 :
	inss_empregado = salario_base*0.11
# Saída
print "O salário base é R$ %.2f" % salario_base
print "O custo mensal para o empregador é de R$ %.2f" % (salario_base + transporte_empregador + fgts_empregador + inss_empregador)
print "O salário líquido que o trabalhador irá receber no mês é R$ %.2f" % (salario_base - (transporte_empregado + inss_empregado))

