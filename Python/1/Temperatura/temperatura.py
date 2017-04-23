# coding: utf-8
# Conversor de Temperaturas
# Felipe Marinho (C) <felipe.marinho@ccc.ufcg.edu.br>

temperatura_fahrenheit = float(raw_input())
temperatura_celsius = ((temperatura_fahrenheit - 32)*(5/9.0))
temperatura_kelvin = (temperatura_celsius + 273.15)
print """Fahrenheit: %.3f F
Celsius: %.3f C
Kelvin: %.3f K""" % (temperatura_fahrenheit, temperatura_celsius, temperatura_kelvin)
