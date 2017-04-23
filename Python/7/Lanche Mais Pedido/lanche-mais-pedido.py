# coding: utf-8
# Lanche Mais Pedido
# Felipe Marinho (C) | 116110223 | <felipe.marinho@ccc.ufcg.edu.br>

def lanchemaispedido(pedidos):
	for e in pedidos:
		mais_pedido = 0
		for f in pedidos:
			if e == f:
				mais_pedido += 1
				if mais_pedido > len(pedidos)/2:
					return e
	return None