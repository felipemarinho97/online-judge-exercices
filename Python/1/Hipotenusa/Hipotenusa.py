# coding: utf-8
# Cálculo de Hipotenusa
# Felipe Marinho (C) <felipe.marinho@ccc.ufcg.edu.br>
a = float(raw_input("Medida do Cateto 1? "))
b = float(raw_input("Medida do Cateto 2? "))
c = (a**2 + b**2)**(1/2.0)
print "Medida da Hipotenusa: %.2f" % c
