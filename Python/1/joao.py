# coding: utf-8
# João

pos_inicial = float(raw_input())
litros_inicial = float(raw_input())
pos_final = float(raw_input())
litros_final = float(raw_input())

dist = pos_final - pos_inicial
delta = litros_inicial - litros_final

print "%.1f" % (dist / delta)
