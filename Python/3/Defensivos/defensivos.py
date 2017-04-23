# coding: utf-8
# Defensivos
# Felipe Marinho (C) | 116110223 | <felipe.marinho@ccc.ufcg.edu.br>

import math

produto = str(raw_input())
area = float(raw_input())

if produto == "Fungicida" :
	print "%i Fungicida(s). %.2f reais." % ((math.ceil(area/50)), ((math.ceil(area/50)*320)))
elif produto == "Herbicida" :
	print "%i Herbicida(s). %.2f reais." % ((math.ceil(area/(1/0.3))), ((math.ceil(area/(1/0.3))*100)))
elif produto == "Inseticida" :
	print "%i Inseticida(s). %.2f reais." % ((math.ceil(area/(30/2.5))), ((math.ceil(area/(30/2.5))*400)))
int1 = 1
contador = 1
for i in contador :
	if contador == type(int1) :
		contador += 1

for i in range(1000000000) :
	
