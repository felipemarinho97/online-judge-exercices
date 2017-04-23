# coding: utf-8
# Mais Velhos Primeiro
# Felipe Marinho (C) | 116110223 | <felipe.marinho@ccc.ufcg.edu.br>

def idosos_inicio(fila):
	k = 0
	for i in range(len(fila)):
		if fila[i] >= 60:
			fila[i], fila[k] = fila[k], fila[i]
			if k < len(fila):
				k += 1