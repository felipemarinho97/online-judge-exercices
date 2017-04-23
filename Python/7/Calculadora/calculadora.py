# coding: utf-8
# Calculadora
# Felipe Marinho (C) | 116110223 | <felipe.marinho@ccc.ufcg.edu.br>

def soma(a,b):
	return int(a) + int(b)

def subtracao(a,b):
	return int(a) - int(b)

def multiplicacao(a,b):
	return int(a) * int(b)

def divisao(a,b):
	if b == '0' or b == 0:
		return "Erro: Divisão por 0"
	return int(a) / int(b)

resultados =[]

while True:
	entrada = raw_input().split()
	if entrada[0] == '1':
		resultados.append(soma(entrada[1],entrada[2]))
	elif entrada[0] == '2':
		resultados.append(subtracao(entrada[1],entrada[2]))
	elif entrada[0] == '3':
		resultados.append(multiplicacao(entrada[1],entrada[2]))
	elif entrada[0] == '4':
		resultados.append(divisao(entrada[1],entrada[2]))
	elif entrada[0] == '5':
		break

for e in resultados:
	print e