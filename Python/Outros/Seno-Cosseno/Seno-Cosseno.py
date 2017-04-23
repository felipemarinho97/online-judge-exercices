# coding: utf-8
# Senos e Cossenos
# Felipe Marinho (C) | 116110223 | <felipe.marinho@ccc.ufcg.edu.br>

import math

angulo = float(raw_input())
salto = float(raw_input())
linhas = int(raw_input())

print "|Angulo|   Seno|Cosseno|"
for i in range(linhas) :
	print "|%6.1f|%.5f|%.5f|" % ((angulo + salto*i), (math.sin(math.radians(angulo + salto*i))), (math.cos(math.radians(angulo + salto*i))))
