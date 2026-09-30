print('-' * 20)
sl = float(input('Qual seu salário atual?\nR$: '))
fl = int(input('Quantos filhos você tem: '))
print('-' * 20)
if fl <= 0:
    perc = 5
    al = sl * 0.05
elif fl>=1 or fl<=2:
    perc = 10
    al = sl * 0.10
elif fl>=3 or fl<=4:
    perc = 15
    al = sl * 0.15
else:
    perc = 20
    al = sl * 0.20

tl = sl + al

print(f'Quantidade de filhos: {fl}')
print(f'Salário antigo: R${sl:.2f}')
print(f'Aumento salarial: R${al:.2f}')
print(f'Percentual aplicado: {perc}%')
print(f'Salário atual: R${tl:.2f}')
print('-' * 20)
