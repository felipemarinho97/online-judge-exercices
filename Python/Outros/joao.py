# coding: utf-8
# Jão
kg = int(raw_input())
nca = int(raw_input())
ncv = int(raw_input())
print "Clientes no atacado = %ikg cada." % (kg / nca)
print "Clientes no varejo = %.2fkg cada." % ((float(kg) % nca) / ncv)
