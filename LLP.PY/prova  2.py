import os 
import time


def limpa_Tela():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def sair():
    input('Clica qualquer botão ...Para sair ')
    limpa_Tela()
    
def erro_numero(mensagem ='ESCOLHA UMA OPÇÃO:'):
    while True:
        nm=input(mensagem)
        try:
            return float(nm)
        except ValueError:
            print(f"Erro: '{nm}' é inválido! Digite apenas números.")
            time.sleep(1)

def menu ():
    print('='*35)
    print('         CALCULADORA SIMPLES')
    print('='*35)
    print(''' 
        1 - Soma

        2 - subtração

        3 - Multiplicação

        4 - Divisão

        5 – Sair ''')
    

    
while True:
    limpa_Tela()
    menu()
    
    opcao=erro_numero()
    
    if opcao == 1:
        limpa_Tela()
        num1=erro_numero('Digete primero numero')
        num2=erro_numero('Digete segundo  numero')
        soma=num1 + num2
        print(f' A soma Do {num1} + {num2 } = {soma}')
        sair()
    elif opcao ==2:
        limpa_Tela()
        num1=erro_numero('Digete primero numero')
        num2=erro_numero('Digete segundo  numero')
        sub=num1-num2
        print(f' A Subtração Do {num1} - {num2 } = {sub}')
        sair()
      
    
    elif opcao ==3:
        limpa_Tela()
        num1=erro_numero('Digete primero numero')
        num2=erro_numero('Digete segundo  numero')
        mul = num1 * num2
        print(f" A multipluicação  do {num1} * {num2} = {mul}")
        sair()
        
    
    elif opcao ==4:
        limpa_Tela()
        num1=erro_numero('Digete primero numero')
        num2=erro_numero('Digete segundo  numero')
        if num2 == 0:
                print("\nErro: Não é possível dividir por zero!")
        else:
            di = num1 / num2
            print(f"divisão : {num1} / {num2} = {di}")  
        sair()   
        
    elif opcao ==5:
        limpa_Tela()
        print("Saindo do Menu.........")
        time.sleep(1)
        break
    else:
        print(f'Essa opção {opcao} não pode ser usada')
        limpa_Tela()