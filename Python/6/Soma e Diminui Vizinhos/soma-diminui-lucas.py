# coding: utf-8

def soma_diminui_vizinhos(lista):
	if len(lista) == 0:
		return 0
	valor = lista[0]
	i = -1
	while True:
		i += 2
		if i > len(lista)-1:
			break
		valor = valor + lista[i]
		if i+1 > len(lista)-1:
			break
		valor = valor - lista[i+1]
	return valor

def soma_diminui_vizinhos2(lista):
	if lista == []:
		return 0
	soma_diminui = lista[0]
	for i in range(1,len(lista),2):
		soma_diminui += lista[i]
		if i+1 > len(lista)-1:
			break
		soma_diminui -= lista[i+1]
	return soma_diminui

lista = [11]
print soma_diminui_vizinhos2(lista)
print soma_diminui_vizinhos(lista)