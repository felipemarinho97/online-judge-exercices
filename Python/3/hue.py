# coding: utf-8
# Melhor Ataque
# Felipe Marinho (C) | 116110223 | <felipe.marinho@ccc.ufcg.edu.br>

times = int(raw_input())
lista_times = []
lista_gols = []
total_gols = 0
maior = -1
for i in range(times) :
	time = raw_input()
	lista_times.append(time)
	gols = int(raw_input())
	lista_gols.append(gols)
	total_gols += gols
	if lista_gols[i] > maior :
		maior = gols
print """Time(s) com melhor ataque (%i gol(s)):""" % maior

for i in range(times) :
	if lista_gols[i] == maior :
		print lista_times[i]

print ""
print "Média de gols marcados: %.1f" % (total_gols/float(times))
