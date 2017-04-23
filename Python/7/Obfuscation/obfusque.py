# coding: utf-8
# Obfuscation
# Felipe Marinho (C) | 116110223 | <felipe.marinho@ccc.ufcg.edu.br>

def troca_troca(palavra):
	import string
	palavra_trocada = ''
	for i in range(len(palavra)):
		if ord(palavra[i]) >= 65 and ord(palavra[i]) <= 90:
			palavra_trocada += string.lower(palavra[i])
		elif ord(palavra[i]) >= 97 and ord(palavra[i]) <= 122:
			palavra_trocada += string.upper(palavra[i])
		else:
			palavra_trocada += palavra[i]
	return palavra_trocada

def meu_in(lista, palavra):
	for i in range(len(lista)):
		if palavra == lista[i]:
			return True
	return False

def encrypt(palavra):
	palavra_encrypt = ''
	l = ["A", "B", "E", "G", "I", "L", "S", "O", "a", "b", "e", "g", "i", "l", "s", "o", "4", "8", "3", "6", "1", "7", "5", "0"]
	for i in range(len(palavra)):
		if meu_in(l,palavra[i]) == True:
			if palavra[i] == "A" or palavra[i] == "a":
				palavra_encrypt += '4'
			elif palavra[i] == "4":
				palavra_encrypt += "A"
			elif palavra[i] == "B" or palavra[i] == "b":
				palavra_encrypt += '8'
			elif palavra[i] == "8":
				palavra_encrypt += "B"
			elif palavra[i] == "E" or palavra[i] == "e":
				palavra_encrypt += '3'
			elif palavra[i] == "3":
				palavra_encrypt += "E"
			elif palavra[i] == "G" or palavra[i] == "g":
				palavra_encrypt += '6'
			elif palavra[i] == "6":
				palavra_encrypt += "G"
			elif palavra[i] == "I" or palavra[i] == "i":
				palavra_encrypt += '1'
			elif palavra[i] == "1":
				palavra_encrypt += "I"
			elif palavra[i] == "L" or palavra[i] == "l":
				palavra_encrypt += '7'
			elif palavra[i] == "7":
				palavra_encrypt += "L"
			elif palavra[i] == "S" or palavra[i] == "s":
				palavra_encrypt += '5'
			elif palavra[i] == "5":
				palavra_encrypt += "S"
			elif palavra[i] == "O" or palavra[i] == "o":
				palavra_encrypt += '0'
			elif palavra[i] == "0":
				palavra_encrypt += "O"
		else:
			palavra_encrypt += palavra[i]
	return palavra_encrypt

def asterixos(palavra):
	palavra_nova = ''
	cont = 0
	for i in range(len(palavra)):
		if palavra[i] == " ":
			palavra_nova += "*"*cont
			cont = 0
		else:
			palavra_nova += palavra[i]
			cont += 1
	return palavra_nova

palavras = []

while True:
	palavra = raw_input()
	if palavra == "fim": break 
	palavras.append(asterixos(encrypt(troca_troca(palavra))))

for i in range(len(palavras)):
	print palavras[i]	