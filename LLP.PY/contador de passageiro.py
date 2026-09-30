tp=0
cont=1
print('=-'*40)
print('CONTADOR DE PASSAGEIROS')
print('=-'*40)
quantidade_viage=int(input('Quantas viagens serão registrado?'))
while cont<=quantidade_viage:
    
    V=int(input(f'viagem {cont}:'))
    tp+=V
    cont+=1
m=tp/quantidade_viage
print('=-'*40)
print('RELATORIO')
print('=-'*40)
print(f'Total passaageiro: {tp}')
print(f'Media por viagem {m:.2f}')
print('=-'*40)