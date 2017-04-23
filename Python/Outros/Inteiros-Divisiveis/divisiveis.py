# coding: utf-8
# Série (8.8)
# Felipe Marinho (C) | 116110223 | <felipe.marinho@ccc.ufcg.edu.br>

a = int(raw_input())
b = int(raw_input())
k = int(raw_input())

for i in range(1,k+1) :
	if i%a == 0 and i%b == 0 :
		print i
