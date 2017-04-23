# coding: utf-8
# Maiores e Menores
# Felipe Marinho (C) | 116110223 | <felipe.marinho@ccc.ufcg.edu.br>

maiores = []
menores = []
pivot = int(raw_input())

while True:
	numero = int(raw_input())
	if numero < 0: break
	if numero <= pivot:
		menores.append(numero)
	else:
		maiores.append(numero)

print menores
print pivot
print maiores