# coding: utf-8
# Primeiro Menor
# Felipe Marinho (C) | 116110223 | <felipe.marinho@ccc.ufcg.edu.br>

def primeiro_menor(num,numeros):
	for i in range(len(numeros)):
		if int(numeros[i]) < num:
			return i
	return -1

def main():
	numeros = raw_input()
	numeros = numeros.split()
	num = int(raw_input())
	indice_menor = primeiro_menor(num,numeros)
	if indice_menor == -1:
		print "sem menores que %i" % num
	else:
		print "primeiro menor que %i: %i" % (num,int(numeros[indice_menor]))

if __name__ == '__main__':
	main()
