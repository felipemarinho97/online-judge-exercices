# coding: utf-8
# Frequência
# Felipe Marinho (C) | 116110223 | <felipe.marinho@ccc.ufcg.edu.br>

def get_frequencia(lista):
	frequencia = []
	iteradas = []
	for e in lista:
		cont = 0
		if not (e in iteradas):
			for f in lista:
				if e == f:
					cont += 1
			frequencia.append(cont)
			iteradas.append(e)
	return frequencia
