from random import randint
compt=randint(0,10)
print('Sou seu computador...')
print('Pensar em um número entre 0 e 10.')
r=int(input('Qual seu palpite?'))
while r!=compt:
    if r<compt:
        print('Mais... Tente mais uma vez.')
        r=int(input('Qual seu palpite?'))
    elif r>compt:
        print('menos... Tente mais uma vez.')
        r=int(input('Qual seu palpite?'))
        if r%2==0:
            t=r-0
print(f'Vocé acertou era {r}.Total de tentaviva {t}')