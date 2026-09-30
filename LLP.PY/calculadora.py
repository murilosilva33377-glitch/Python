import os
import time

def limpa_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    print('=-' * 35)
    print("=== CALCULADORA SIMPLES ===")
    print('=-' * 35)
    print("""    [1] Somar (+)
    [2] Subtrair (-)
    [3] Multiplicar (*)
    [4] Dividir (/)
    [5] Sair""")
    print('=-' * 35)

def sair():
    input("\nPressione Enter para voltar ao menu...")
    limpa_tela()

def erro_numeros(mensagem='Digite um número: '):
    while True:
        nm = input(mensagem).strip()
        try:
            return float(nm) 
        except ValueError:
            print(f"Erro: '{nm}' é inválido! Digite apenas números.")
            time.sleep(1)

while True:
    limpa_tela()
    menu()
    opcao = erro_numeros("Escolha uma opção (1 a 5): ")
    
    opcao = int(opcao) 

    
    if opcao:
        limpa_tela()
        
        operacoes = {1: "Soma", 2: "Subtração", 3: "Multiplicação", 4: "Divisão"}
        print(f"=== Operação de {operacoes[opcao]} ===")
        
        num1 = erro_numeros("Digite o primeiro número: ")
        num2 = erro_numeros("Digite o segundo número: ")

        if opcao == 1:
            resultado = num1 + num2
            print(f"\nResultado: {num1} + {num2} = {resultado}")
        
        elif opcao == 2:
            resultado = num1 - num2
            print(f"\nResultado: {num1} - {num2} = {resultado}")
        
        elif opcao == 3:
            resultado = num1 * num2
            print(f"\nResultado: {num1} * {num2} = {resultado}")
        
        elif opcao == 4:
            if num2 == 0:
                print("\nErro: Não é possível dividir por zero!")
            else:
                resultado = num1 / num2
                print(f"\nResultado: {num1} / {num2} = {resultado}")      
        
        sair()

    elif opcao == 5:
        print("\nSaindo da calculadora... Até mais!")
        time.sleep(1)
        break  
    
    else:
        print("Opção inválida! Escolha um número de 1 a 5.")
        time.sleep(1)
