# coding: utf-8
# Subtração de Polinômios
# Felipe Marinho (C) | 116110223 | <felipe.marinho@ccc.ufcg.edu.br>


def subtrai_polinomios(p1,p2):
	if p2 == []:
		return p1
	subtrai_polinomios = []
	for i in range(len(p2)):
		try:
			subtrai_polinomios.append(p1[i]-p2[i])
		except IndexError:
			subtrai_polinomios.append(-p2[i])
	for i in range(len(subtrai_polinomios)-1,-1,-1):
		if subtrai_polinomios[i] == 0:
			subtrai_polinomios.pop(i)
		else:
			break
	return subtrai_polinomios
