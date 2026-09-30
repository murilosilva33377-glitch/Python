saldo=1000
while True:
    print('_'*20)
    print(' '*5,'Bem vindo ao \n Banco dos pobres ')
    print('_'*20)
    op=int(input('''
    [1]consulta salario
    [2]realiaze sauqe
    [3]depositar
    [4]sair do sistema                
    escolha uma opção:'''))
    if op==1:
        print(f'seu salario atula é R${saldo}')
    elif op==2:
        valor_saque = float(input("Informe o valor do saque: R$ "))
        if valor_saque <= saldo and valor_saque > 0:
            saldo -= valor_saque
            print(f"Saque realizado com sucesso! Novo saldo: R$ {saldo:.2f}")
        elif valor_saque <= 0:
            print("Valor de saque inválido. Digite um valor positivo.")
        else:
            print("Erro: Saldo insuficiente para realizar esta operação.")
    elif op ==3:
        deposito = float(input("Informe o valor do deposito: R$ "))
        saldo=saldo+deposito
        print(f'Seu saldo aumento para R${saldo:.2f}')
    elif op == '4':
        print("Encerrando o sistema. Obrigado por utilizar nosso banco!")
        break    
    else:
        print("Opção inválida. Por favor, escolha 1, 2 ou 3.")