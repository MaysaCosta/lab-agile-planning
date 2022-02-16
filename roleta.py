#################################################################
# BMM0580 ICB-IME 2012                                          # 
# Prof Roberto Cesar                                            #
#                                                               #
# Primeiro Exercicio Programa -- Roleta                         # 
#                                                               # 
# Camyla T Romao         7995201                                #
# Maysa Archinto I Costa 8084882                                # 
#                                                               # 
# Informacoes sobre Desenvolvimento:                            # 
# Ambiente: Editor de texto                                     #  
# Sistema Operacional: Mac                                      #
#################################################################

# Programa em Python que avalia o rendimento de um jogador atraves da entrada das informacoes sobre a quantia apostada e os numeros apostado e sorteado em cada rodada

entrada=raw_input('> ')
numeros_separados=entrada.split()
quantia_apostada=int(numeros_separados[0])
numero_apostado=int(numeros_separados[1])
numero_sorteado=int(numeros_separados[2])

# Atribuicoes:
saldo=0 # Variavel que calcula o saldo obtido em cada rodada
saldototal=0 # Variavel que soma o saldo total do jogador
cont=1 # Identifica o numero da rodada

while (quantia_apostada!=0 or numero_apostado!=0 or numero_sorteado!=0):
# Condicao criada para garantir a finalizacao do programa quando o usuario digitar a entrada '0 0 0'
	
	if (numero_apostado>38 or numero_sorteado>38):
		cont=cont-1
		print '# ?!'

	elif (numero_apostado<1 or numero_sorteado<1):
		cont=cont-1
		print '# ?!'
 
# Os numeros apostado e sorteado devem estar entre 1 e 38

	elif (numero_apostado==numero_sorteado):
		saldo=6*quantia_apostada
		saldototal=saldototal+saldo
		regra=1
		print '# '+str(cont)+' '+str(regra)+' '+str(saldo)
# Quando o apostador acertar o numero sorteado, ele recebe seis vezes a quantia apostada

	elif (numero_apostado/10==numero_sorteado/10):
		saldo=3*quantia_apostada
		regra=2
		saldototal=saldototal+saldo
		print '# '+str(cont)+' '+str(regra)+' '+str(saldo)
# Quando o apostador acertar a dezena do numero sorteado, ele recebe tres vezes a quantia apostada

	elif (numero_apostado%2==0 and numero_sorteado%2==0):
		saldo=quantia_apostada
		regra=3		
		saldototal=saldototal+saldo
		print '# '+str(cont)+' '+str(regra)+' '+str(saldo)
# Quando o apostador apostar num numero par e o numero sorteado tambem for par, ele recebe exatamente a quantia apostada

	elif (numero_apostado%2!=0 and numero_sorteado%2!=0):
		saldo=quantia_apostada
		regra=3		
		saldototal=saldototal+saldo
		print '# '+str(cont)+' '+str(regra)+' '+str(saldo)
# Quando o apostador apostar num numero impar e o numero sorteado tambem for impar, ele recebe exatamente a quantia apostada

	else:
		regra=0
		saldo=-quantia_apostada
		saldototal=saldototal+saldo
		print '# '+str(cont)+' '+str(regra)+' '+str(saldo)
# Caso nenhuma das condicoes tenha ocorrido e o apostador erre totalmente o numero sorteado, ele nao recebe nada

	cont=cont+1
	entrada=raw_input('> ')
	numeros_separados=entrada.split()
	quantia_apostada=int(numeros_separados[0])
	numero_apostado=int(numeros_separados[1])
	numero_sorteado=int(numeros_separados[2])
# Os comandos acima garantem a continuidade do laco	
	
print '# '+str(saldototal)
