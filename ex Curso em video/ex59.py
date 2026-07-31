print('=-'*15)
n1=float(input('Primero valor:'))
n2=float(input('Segundo valor:'))
print('=-'*15)
while True:
    op=int(input('''
    [1]somar
    [2]multiplicar
    [3]maior
    [4]novos número
    [5]sair do programa
>>>>>Escolha um opção:'''))
    print('=-'*15)
    if op==1:
        print(f'A soma entre {n1}+{n2} é {n1+n2}')