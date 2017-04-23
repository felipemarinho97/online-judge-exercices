# coding: utf-8
# Prof Equações
# Felipe Marinho (C) | 116110223 | <felipe.marinho@ccc.ufcg.edu.br>

a = float(raw_input())
b = float(raw_input())
c = float(raw_input())
delta = (b**2)-(4*a*c)

if delta > 0 :
	print "x1 = %.2f\nx2 = %.2f" % ((-b + (delta)**(1/2.0)) / (2*a), (-b - (delta)**(1/2.0)) / (2*a))

elif delta == 0 :
	print "x = %.2f" % ((-b + (delta)**(1/2.0)) / (2*a))
elif delta < 0 :
	print "sem raizes reais"

