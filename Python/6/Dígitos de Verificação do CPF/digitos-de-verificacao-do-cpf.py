# coding: utf-8
# Dígitos de Verificação do CPF
# Felipe Marinho (C) | 116110223 | <felipe.marinho@ccc.ufcg.edu.br>

def calcula_digitos_verificacao(digitos):
	def verificacao(digitos):
		mult = 0
		j = -1
		for i in range(2,len(digitos)+2,1):
			mult += int(digitos[j])*i
			j -= 1
		digito = (mult*10) % 11
		if digito == 10:
			return "0"
		else:
			return str((mult*10) % 11)
	digito1 = verificacao(digitos)
	digitos_verificadores = digito1+verificacao(digitos+digito1)
	return digitos_verificadores

assert calcula_digitos_verificacao('153245875') == '40'