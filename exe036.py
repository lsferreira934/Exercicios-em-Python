from pygame import mixer
import time
mixer.init()


cores ={'azulback':'\033[7;40m',
        'piscina':'\033[1;36m',
        'limpa':'\033[m',
        'negrito':'\033[1m',
        'vermelho':'\033[1;31m',
        'verde':'\033[7;32m',
        'vermelhoblack':'\033[7;31m'}
print('\033[1;36m-=\033[m' * 30)
print('                   {}EMPRÉSTIMOS DO SILVIO{}'.format(cores['piscina'], cores['limpa']))
print('\033[1;36m-=\033[m' * 30)
#INFORMAÇÕES DO CLIENTE
nome = str(input('>Digite o seu nome completo: ')).strip().upper()
idade = int(input('>Digite a sua idade: '))
casa = float(input('>Digite o valor do imovel: '))
salario = float(input('>Digite a sua renda mensal: '))
prazo = int(input('>Digite em quantos anos quer pagar: '))

if salario <= 0 or casa <= 0 or prazo <= 0:#SE USUARIO DIGITAR EM SALÁRIO E CASA
    print('{}>Cliente REPROVADO<{}'.format(cores['vermelhoblack'], cores['limpa']))
    print('{}>Informações erradas ou zeradas{}<'.format(cores['negrito'], cores['limpa']))
    input('{}OBRIGADO POR ULTILIZAR O PROGRAMA{}!'.format(cores['negrito'], cores['limpa']))
    time.sleep(360)


    #import os
    #os.system("pause")
mixer.music.load('piao.mp3')
mixer.music.play()
time.sleep(3)
print('Verificando as informações...')
time.sleep(3)
print('Contando o dinheiro do Silvio....')
time.sleep(3)
print('Somando as dividas do jequiti...')
time.sleep(3)
print('Mandando para o Silvio aprovar...')
time.sleep(3)
print('PRONTO!')
time.sleep(3)


#CALCULOS DAS INFORMAÇÕES DO CLIENTE
cond1 = (salario * 30 / 100) #30% SALÁRIO
cond2 = (prazo * 12)         #ANO DIVIDO EM MESES
cond3 = (casa / cond2)       #VALOR DA CASA DIVIDIDO PELOS MESES
print('\033[1;36m-=\033[m' * 30)

if idade <= 17: # SE O CLIENTE NÃO POSSUI A IDADE MINIMA
    mixer.music.load('naodeu.mp3')
    mixer.music.play()
    print('{}>Cliente REPROVADO<{}'.format(cores['vermelhoblack'], cores['limpa']))
    print('{}>Não possui a IDADE minima{}<'.format(cores['negrito'],cores['limpa']))


elif cond1 == 1 or cond2 == 1 or cond3 == 1:#SE USUARIO DIGITAR EM SALÁRIO E CASA
    print('{}>Cliente REPROVADO<{}'.format(cores['vermelhoblack'], cores['limpa']))
    print('{}>Informações erradas ou zeradas{}<'.format(cores['negrito'], cores['limpa']))

elif idade >=18 and cond3 < cond1: #SE O CLIENTE TEM SALARIO SUFICIENTE E TEM A IDADE MINIMA
    print('{}>EMPRESTIMO APROVADO!<{}'.format(cores['verde'], cores['limpa']))
    print('{}>Salário = R${:.2f}<{}'.format(cores['negrito'], salario, cores['limpa']))
    print('{}>Valor a financiar = R${:.2f}<{}'.format(cores['negrito'], casa, cores['limpa']))
    print('{}>Valor da parcela = R${:.2f}<{}'.format(cores['negrito'], cond1, cores['limpa']))

elif cond3 > cond1 and cond1 < cond3: #SE O CLIENTE NÃO TEM SALÁRIO SULFICIENTE
    print('{}>EMPRESTIMO NEGADO!<{}'
          '\n{}>Infelizmente você não pode financiar esse imovel<{} '
          '\n{}>[o cliente ultrapassou o limite de 30% da sua renda]<{}'.format(cores['vermelhoblack'], cores['limpa'], cores['negrito'],cores['limpa'], cores['vermelho'], cores['limpa']))
    print('{}>Salário = R${:.2f}<{}'.format(cores['negrito'], salario, cores["limpa"]))
    print('{}>Valor a financiar = R${:.2f}<{}'.format(cores['negrito'], casa, cores['limpa']))
    print('{}>valor da parcela = R${:.2f}<{}'.format(cores['negrito'], cond1, cores['limpa']))
print('\033[1;36m-=\033[m'* 30)

