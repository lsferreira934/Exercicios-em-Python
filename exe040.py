import random
print('\033[1;36m*-\033[m' * 20)
print('\033[1;35m           CALCULO DE MÉDIA\033[M')
print('\033[1;36m*-\033[m' * 20)
aluno1 = str(input('NOME: ')).upper().strip()
aluno2 = str(input('NOME: ')).upper().strip()
aluno3 = str(input('NOME: ')).upper().strip()
nota1 = float((random.randint(1, 10)) + (random.randint(1, 10))) / 2
nota2 = float((random.randint(1, 10)) + (random.randint(1, 10))) / 2
nota3 = float((random.randint(1, 10)) + (random.randint(1, 10))) / 2
print('\033[1;36m*-\033[m' * 20)

if nota1 >= 7:
    print('\033[1mO aluno\033[m \033[1;34m{}\033[m \033[1mfoi\033[m \033[1;32mAPROVADO\033[m \033[1mcom a nota\033[m \033[1;34m{}\033[m'.format(aluno1, nota1))
elif nota1 == 6.5 or nota1 == 6.0 or nota1 == 5.5 or nota1 == 5.0:
    print('\033[1mO aluno\033[m \033[1;34m{}\033[m \033[1mesta de\033[m \033[1;35mRECUPERAÇÃO\033[m \033[1mpor tirar\033[m \033[1;34m{}\033[m'.format(aluno1, nota1))
else:
    print('\033[1mO aluno\033[m \033[1;34m{}\033[m \033[1mesta\033[m \033[1;31mREPROVADO\033[m \033[1mpor tirar\033[m \033[1;34m{}\033[m'.format(aluno1, nota1))


if nota2 >= 7:
    print('\033[1mO aluno\033[m \033[1;34m{}\033[m \033[1mfoi\033[m \033[1;32mAPROVADO\033[m \033[1mcom a nota\033[m \033[1;34m{}\033[m'.format(aluno2, nota2))
elif nota2 == 6.5 or nota2 == 6.0 or nota2 == 5.5 or nota2 == 5.0:
    print('\033[1mO aluno\033[m \033[1;34m{}\033[m \033[1mesta de\033[m \033[1;35mRECUPERAÇÃO\033[m \033[1mpor tirar\033[m \033[1;34m{}\033[m'.format(aluno2, nota2))
else:
    print('\033[1mO aluno\033[m \033[1;34m{}\033[m \033[1mesta\033[m \033[1;31mREPROVADO\033[m \033[1mpor tirar\033[m \033[1;34m{}\033[m'.format(aluno2, nota2))

if nota3 >= 7:
    print('\033[1mO aluno\033[m \033[1;34m{}\033[m \033[1mfoi\033[m \033[1;32mAPROVADO\033[m \033[1mcom a nota\033[m \033[1;34m{}\033[m'.format(aluno3, nota3))
elif nota3 == 6.5 or nota3 == 6.0 or nota3 == 5.5 or nota3 == 5.0:
    print('\033[1mO aluno\033[m \033[1;34m{}\033[m \033[1mesta de\033[m \033[1;35mRECUPERAÇÃO\033[m \033[1mpor tirar\033[m \033[1;34m{}\033[m'.format(aluno3, nota3))
else:
    print('\033[1mO aluno\033[m \033[1;34m{}\033[m \033[1mesta\033[m \033[1;31mREPROVADO\033[m \033[1mpor tirar\033[m \033[1;34m{}\033[m'.format(aluno3, nota3))

print('\033[1;36m*-\033[m' * 20)