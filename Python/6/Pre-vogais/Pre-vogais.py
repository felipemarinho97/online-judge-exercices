# coding: utf-8
# Pre-vogais
# Felipe Marinho (C) | 116110223 | <felipe.marinho@ccc.ufcg.edu.br>

def meu_in(lista,termo):
	for i in range(len(lista)):
		if lista[i] == termo:
			return True
	return False

def pre_vogais(palavra):
	pre_vogais = []
	vogais = "aeiouAEIOU"
	for i in range(1,len(palavra)):
		if meu_in(vogais,palavra[i]) == True and meu_in(pre_vogais,palavra[i-1]) == False:
			pre_vogais.append(str.lower(palavra[i-1]))
	return pre_vogais

assert pre_vogais("Andrade") == ['r', 'd']
assert pre_vogais("exemplo") == ['x', 'l']
assert pre_vogais("hiaTO") == ['h', 'i', 't']
assert pre_vogais("Arara") == ['r']   