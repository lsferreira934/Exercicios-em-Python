import color, time
from pygame import mixer, event
mixer.init()
mixer.music.load('piao.mp3')
mixer.music.play()
print(color.magenta('-=' * 20))
print(color.yellow('       \033[1mÉ MAIOR, MENOR OU IGUAL?\33[m'))
print(color.magenta('-=' * 20))
num1 = int(input(color.green('>DIGITE UM NÚMERO INTEIRO: ')))
num2 = int(input(color.blue('>DIGITE OUTRO NÚMERO INTEIRO: ')))
print(color.magenta('-=' * 20))
print(color.blue('PROCESSANDO A BAGAÇA...'))
time.sleep(3)
print(color.magenta('-=' * 20))
if num1 > num2:
    print('>O NÚMERO {} É  MAIOR QUE O NÚMERO {}'.format(num1, num2))
elif num2 > num1:
    print('>O NÚMERO {} É MAIOR QUE O NÚMERO {}'.format(num2, num1))
else:
    mixer.music.load('naodeu.mp3')
    mixer.music.play()
    print('\033[1;31m>NÃO EXISTE VALOR MAIOR, OS DOIS SÃO IGUAIS.\033[m')

print(color.magenta('-=' * 20))
time.sleep(7)