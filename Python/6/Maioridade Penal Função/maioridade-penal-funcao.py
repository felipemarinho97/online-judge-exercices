# coding: utf-8
# Maioridade Penal Função
# Felipe Marinho (C) | 116110223 | <felipe.marinho@ccc.ufcg.edu.br>

def maioridade_penal(nomes,idades):
	idades = idades.split()
	nomes = nomes.split()
	maiores_de_idade = ""
	for i in range(len(nomes)):
		if int(idades[i]) >= 18:
			maiores_de_idade += nomes[i] + " "
	return maiores_de_idade[:-1]