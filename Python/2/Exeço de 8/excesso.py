# coding: utf-8
# Excesso de 8
# Felipe Marinho (C) | 116110223 | <felipe.marinho@ccc.ufcg.edu.br>

binario = raw_input()
print "%i" % ((int(binario[-1])*2**0) + (int(binario[-2])*2**1) + (int(binario[-3])*2**2) + (int(binario[-4])*2**3) - 8)
