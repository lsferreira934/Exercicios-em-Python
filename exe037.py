import color
print(color.blue('-=' * 20))
print(color.green('CALCULADORA DE HEXADECIMAL - OCTAL - BINÁRIO'))
print(color.blue('-=' * 20))

num = int(input('Digitite um número qualquer que seja inteiro: '))
print(color.blue('-=' * 20))
print(color.yellow('[1] HEXADECIMAL '))
print(color.red('[2] OCTAL'))
print(color.green('[3] BINÁRIO'))
print(color.blue('-=' * 20))
opcao = int(input('Escolha uma das opções: '))
print(color.blue('-=' * 20))
if opcao == 1:
    print(color.yellow(' O numero {} convertido para HEXADECIMAL É {}'.format(num, hex(num)[2:])))
elif opcao == 2:
    print(color.red('O numero {} convertido para OCTAL é {}'.format(num, oct(num)[2:])))
elif opcao == 3:
    print(color.green('O numero {} convertido para BINÁRIO é {}'.format(num, bin(num)[2:])))
else:
    print('\033[2;30;41mOPÇÃO INVALIDA\033[m')
print(color.blue('-=' * 20))



