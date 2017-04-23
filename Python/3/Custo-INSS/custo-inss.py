# coding: utf-8
# Custo INSS
# Felipe Marinho (C) | 116110223 | <felipe.marinho@ccc.ufcg.edu.br>

salario = float(raw_input())

contrubuicao_empregador = salario*0.12
if salario >= 0 and salario <= 1317.07 :
	contrubuicao_trabalhador = salario*0.08
elif salario >= 1317.08 and salario <= 2195.12 :
	contrubuicao_trabalhador = salario*0.09
elif salario > 2195.12 :
	contrubuicao_trabalhador = salario*0.11
print """O valor da contribuição do INSS a ser pago pelo empregador é de R$ %.2f
O valor da contribuição do INSS a ser pago pelo empregado é de R$ %.2f""" % (contrubuicao_empregador, contrubuicao_trabalhador)
