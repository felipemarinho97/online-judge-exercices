# coding: utf-8
# Densidade
# Felipe Marinho (C) | 116110223 | <felipe.marinho@ccc.ufcg.edu.br>
massa_1 = float(raw_input())
volume_1 = float(raw_input())
massa_2 = float(raw_input())
volume_2 = float(raw_input())
massa_3 = float(raw_input())
volume_3 = float(raw_input())

if massa_1/volume_1 < massa_2/volume_2 and massa_1/volume_1 < massa_3/volume_3 :
	liquido = 1
	densidade = massa_1/volume_1
elif massa_2/volume_2 < massa_1/volume_1 and massa_2/volume_2 < massa_3/volume_3 :
	liquido = 2
	densidade = massa_2/volume_2
elif massa_3/volume_3 < massa_2/volume_2 and massa_1/volume_1 > massa_3/volume_3 :
	liquido = 3
	densidade = massa_3/volume_3

print "O líquido %s, com densidade %.2f, irá ocupar a parte de cima do recipiente." % (liquido, densidade)
