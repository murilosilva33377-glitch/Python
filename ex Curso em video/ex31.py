dis=float(input('Qual é a distacia da sua viagem: '))
if dis<=200:
    pr=dis*0.50
else:
    pr=dis*0.45
print(f'Sua viagem ficara R${pr:.2f}')