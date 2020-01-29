from datetime import date
from pygame import mixer
from time import sleep
import color
mixer.init()
mixer.music.load('1942.mp3')
mixer.music.play()
print('\033[1;31m-=\033[m' * 20)
print('\033[1m          VOCÊ JÁ SE ALISTOU?\033[m')
print('\033[1;31m=-\033[m' *20)

ano = int(input('\033[1mDIGITE O ANO EM QUE VOCÊ NASCEU:\033[m '))
pc = date.today().year
passou = (pc - ano) - 17
falta = 17 - (pc - ano)
print('\033[1;31m=-\033[m' *20)
print('\033[1m         BUSCANDO INFORMAÇÕES....\033[m')
sleep(3)
print('\033[1m         OBTENDO LINK....\033[m')
sleep(3)
print('\033[1m    BUSCAS REALIZDAS COM SUCESSO!!\033[m')
sleep(3)
print('\033[1;31m=-\033[m' *20)
if (pc - ano) == 18:
    print('\033[1;32m        SEJA BEM-VINDO SOLDADO!!\033[m')

elif (pc - ano) <= 17:
    print('\033[1;33m   TE ESPERAMOS NO FUTURO SOLDADO!!\033[m')
    print('\033[1m          AINDA FALTA {} ANOS \033[1m'.format(falta))
else:
    print('\033[1;31m  JÁ PASSOU DA DATA LIMITE SOLDADO!!\033[m')
    print('\033[1m          PASSOU {} ANOS\033[1m'.format(passou))
print('\033[1;31m=-\033[m' *20)