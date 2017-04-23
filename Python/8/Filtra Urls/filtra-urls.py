# coding: utf-8
# Filtra Urls
# Felipe Marinho (C) | 116110223 | <felipe.marinho@ccc.ufcg.edu.br>

def filtra_urls(l):
	filtra = []
	for i in range(len(l)):
		for j in range(len(l[i])-9):
			if l[i][j] == "g":
				if l[i][j+1] == 'o' and l[i][j+2] == "o" and l[i][j+3] == "g" and l[i][j+4] == "l" and l[i][j+5] == "e" and l[i][j+6] == "." and l[i][j+7] == "c" and l[i][j+8] == "o" and l[i][j+9] == "m":
					filtra.append(l[i])
	return filtra