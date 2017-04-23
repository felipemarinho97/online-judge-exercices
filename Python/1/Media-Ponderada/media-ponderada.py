# coding: utf-8
# Media Ponderada
# Felipe Marinho (C) <felipe.marinho@ccc.ufcg.edu.br>

nota1 = float(raw_input())
nota2 = float(raw_input())
nota3 = float(raw_input())

peso_nota1 = float(raw_input())/100
peso_nota2 = float(raw_input())/100

print "Média Final: %.1f" % (nota1*peso_nota1 + nota2*peso_nota2 + nota3*(1 - (peso_nota1 + peso_nota2)))

