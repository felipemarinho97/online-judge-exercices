# coding: utf-8
# Status Unidade
# Felipe Marinho (C) | 116110223 | <felipe.marinho@ccc.ufcg.edu.br>

quantidade_de_mtps = int(raw_input())

if quantidade_de_mtps == 1:
	nota1 = float(raw_input())
	media = nota1
	print "%.1f" % media
	print "Aluno ainda não aprovado na unidade"
elif quantidade_de_mtps == 2:
	nota1 = float(raw_input())
	nota2 = float(raw_input())
	media = (nota1+nota2)/2.0
	print "%.1f" % media
	if media < 6:
		print "Aluno ainda não aprovado na unidade"
	else:
		print "Aluno aprovado na unidade"
elif quantidade_de_mtps == 3:
	nota1 = float(raw_input())
	nota2 = float(raw_input())
	nota3 = float(raw_input())
	media = ((nota1+nota2+nota3)/3.0)-0.5
	print "%.1f" % media
	if media < 6:
		print "Aluno ainda não aprovado na unidade"
	else:
		print "Aluno aprovado na unidade"
elif quantidade_de_mtps == 4:
	nota1 = float(raw_input())
	nota2 = float(raw_input())
	nota3 = float(raw_input())
	nota4 = float(raw_input())
	media = ((nota1+nota2+nota3+nota4)/4.0)-0.5
	print "%.1f" % media
	if media < 6:
		print "Aluno ainda não aprovado na unidade"
	else:
		print "Aluno aprovado na unidade"