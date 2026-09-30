print('=-'*40)
print('consumo de comnbustivo')
print('=-'*40)
n=str(input('Digite o nome: ')).strip().upper()[0]
q=float(input('Quanto quilometros prercorridos:'))
l=float(input('Quantos listros vocé utilizar:'))
print('=-'*40)
c=q/l
if c<8:
    s='alto cunsumo'
elif c<=12:
    s='consumo normal'
else:
    s='consumo ecomico'
print('=-'*40)
print('RESUTADO')
print('=-'*40)
print(f'Motorista {n}')
print(f'Consumo {c:.2f} km/h')
print(f'Classificação {s}')