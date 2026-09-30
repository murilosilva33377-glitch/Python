import os
import time
saldo = 1000.0
def limpa_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def sair():
    input("\nPressione Enter para voltar ao menu...")
    
    

def erro_numeros(mensagem='Digite um número: '):
    while True:
        nm = input(mensagem).strip()
        try:
            return float(nm) 
        except ValueError:
            print(f"Erro: '{nm}' é inválido! Digite apenas números.")
            

def menu():
    print('=-' * 35)
    print("=== Bank 2A ===")
    print('=-' * 35)
    print("""    [1]-Consultar saldo
    [2]-Depositar
    [3]-Sacar
    [4]-Sair
   """)
    print('=-' * 35)
    

while True:
    limpa_tela()
    menu()
    opcao = erro_numeros("Escolha uma opção (1 a 4): ")
    opcao = int(opcao)

    if opcao:
        limpa_tela()

        tema={1: "Consultar saldo", 2: "Depositar", 3: "Sacar",4: "Sair"}
        print(f"=== {tema[opcao]} ===")

        if opcao == 1:
            if not saldo:
                print("O saldo está zerado.")
            print(f"\nSeu saldo atual é: R$ {saldo:.2f}")
            

        elif opcao == 2:
            deposito = erro_numeros("Digite o valor a ser depositado: R$ ")
            saldo += deposito
            print(f"\nDepósito realizado com sucesso! Novo saldo: R$ {saldo:.2f}")
            
        elif opcao == 3:
            saque = erro_numeros("Digite o valor a ser sacado: R$ ")
            if saque > saldo:
                print("\nSaldo insuficiente para realizar o saque.")
            else:
                saldo -= saque
                print(f"\nSaque realizado com sucesso! Novo saldo: R$ {saldo:.2f}")
            
        elif opcao == 4:
            print("\nSaindo do programa...")
            time.sleep(1)
            break
        sair()
    else:
        print("Opção inválida! Tente novamente.")
        sair()
        time.sleep(1)