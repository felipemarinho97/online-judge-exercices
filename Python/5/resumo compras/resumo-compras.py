# coding: utf-8
# Resumo Compras
# Felipe Marinho (C) | 116110223 | <felipe.marinho@ccc.ufcg.edu.br>

compras = []
valor_total = 0
produto_mais_caro = 0

while True:
        precos = raw_input()
        if precos == "fim":
                break
        else:
                compras.append(float(precos))
		valor_total += float(precos)
		if produto_mais_caro < compras[-1]:
			produto_mais_caro = float(precos)


print "O valor médio por produto foi R$ %.2f. O produto mais caro custa R$ %.2f." % ((valor_total/float(len(compras))), produto_mais_caro)

