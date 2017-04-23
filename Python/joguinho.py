# coding: utf-8
# Em busca do SHopping
# Felipe Marinho (C) | <felipe.marinho@ccc.ufcg.edu.br>

import time

nome = raw_input("Digite seu nome: ")
crush = raw_input("Digite o nome do crush: ")
print "\nSão 6:00 horas da manhã.."
time.sleep(2)
print "%s acabou de acordar..\n" % nome
time.sleep(2)
print "De repente o você escuta o batulho do Whatsapp.. quem será a esta hora?!"
print "(1) %s. (2) Ninguém, sou mt alone pra falar com alguém. (3) Minha mãe." % crush 
time.sleep(2)
escolha = raw_input("Digite o número: ")
def historia():
	print "O seu crush lhe dá um belo e radiante 'Bom diaaa'.."
	time.sleep(3)
	print "Ele lhe convida pra sair para algum lugar.."
	time.sleep(3)
	print "Você fica nervoso(a).."
	time.sleep(2)
	lugar = raw_input("Para onde vocês dois irão sair? ")

if escolha == "1":
	historia()
elif escolha == "2":
	print "De repente você escuta novamente o barulhinho.."
	time.sleep(2)
	print "Não pode ser!! Você limpa bem os olhos e olha a aba de notificações.."
	time.sleep(4)
	print "Lá está escrito o nome de %s." % crush
	time.sleep(5)
	print "Você não consegue acreditar.. só pode ser seu dia de sorte!!"
	time.sleep(2)
	historia()
elif escolha == "3":
	print "Acoooorda que tá na hr da aula!"
	time.sleep(2)
	print "Você vai para a aula e o inesperado acontece...."
	time.sleep(3)
	historia()