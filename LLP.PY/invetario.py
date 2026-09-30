import os
import time

def limpa_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

item=[]
quantidade=[]

def menu():
    print('=-' * 35)
    print("=== Menu de Opções ===")
    print('=-' * 35)
    print("""    [1] Consutar estoque
    [2] Adicionar item do estoque
    [3] Remover item do estoque
    [4] Sair""")
    print('=-' * 35)

def sair():
        input("\nPressione Enter para voltar ao menu...")
        limpa_tela()

def erro_letras():
    while True:
        nome = input('Digite o nome do item: ').strip()
        if nome.replace(" ", "").isalpha() and nome != "": 
            return nome
        else:
            print(f"Erro: '{nome}' é inválido! Digite apenas letras.")
            time.sleep(1)

def erro_numeros(mensagem='Digite apenas números: '):
    while True:
        nm = input(mensagem).strip()
        try:
            return int(nm)
        except ValueError:
            print(f"Erro: '{nm}' é inválido! Digite apenas números.")
            time.sleep(1)

while True:
    limpa_tela()
    menu()
    opençao = erro_numeros("Escolha uma opção (1 a 4): ")
    
 
    if opençao == 1:
        limpa_tela()
        print("=== Estoque Atual ===")
        if not item:
            print("O estoque está vazio.")
        else:
            for i in range(len(item)):
                print(f"Item: {item[i]} | Quantidade: {quantidade[i]}")
        time.sleep(1)
        sair() 
    elif opençao == 2:
        limpa_tela()
        print("=== Adicionar Item ao Estoque ===")
        nome_item = erro_letras()
        quantidade_item = erro_numeros("Digite a quantidade: ")
        
        item.append(nome_item)
        quantidade.append(quantidade_item)
        print(f"\nItem '{nome_item}' adicionado com sucesso!|Quantidade: {quantidade_item}")
        time.sleep(0.5)
    elif opençao == 3:
        limpa_tela()
        print("=== Remover Item do Estoque ===")
        print(f"Itens disponíveis no estoque:{', '.join(item)}")
        nome_item = erro_letras()
        if nome_item in item:
            index = item.index(nome_item)
            del item[index]
            del quantidade[index]
            print(f"\nItem '{nome_item}' removido com sucesso!")
        elif not item:
            print("O estoque está vazio. Nenhum item para remover.")
        else:
            print(f"\nItem '{nome_item}' não encontrado no estoque.")
        time.sleep(1)
        sair()
    elif opençao == 4:
        print("Saindo do programa...")
        time.sleep(1)
        break
    else:
        print("Opção inválida! Tente novamente.")
        sair()
        time.sleep(1)