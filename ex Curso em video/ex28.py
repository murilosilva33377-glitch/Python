from random import randint
com=randint(0,5)
print('__'*10)
print('Pensei em um numero aletorio')
print('__'*10)
ply=int(input('escolha um numero de 0 a 5:\n'))
if ply == com:
    print('Você acerto parabens!!!!')
elif ply>5:
    print('Não existe esse numero')
elif ply:
    print(F'Que pena você errou era {com} não era {ply}')
