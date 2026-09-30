print('=-'*40)
n=str(input('Digete seu nome:'))
h=float(input('Informe o seu horario de saida:'))
if h>=2:
    vp=10.00
elif h<=5:
    vp=20.00
else:
    vp=30.00
print('=-'*40)
print(' '*10,'RESULTADO')
print('=-'*40)
print(f'Clinete {n}')
print(f'horario de saida: {h}')
print(f'Saldo R${vp}')