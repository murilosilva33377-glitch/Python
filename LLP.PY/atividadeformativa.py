import os
import time

item=[]
quantidade=[]
Preço=[]
def limpa_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    print('=-'*35)
    print('===sistema de inveterio===')
    print('=-'*35)
    print("""   
        [1] Cadastro produto
        [2] Lista produto
        [3] Busca produto 
        [4] Remover produto 
        [5] Sair""")
    print('=-' * 35)

def erro_letras():
    while True:
        nome = input('Digite o nome do item: ').strip().lower()
        if nome.replace(" ", "").isalpha() and nome != "": 
            return nome
        else:
            print(f"Erro: '{nome}' é inválido! Digite apenas letras.")
            time.sleep(1)

def erro_preco(mensagem='Digite o preço R$: '):
    while True:
        nm = input(mensagem).strip().replace(',', '.')
        try:
            return float(nm)
        except ValueError:
            print(f"Erro: '{nm}' é inválido! Digite um preço válido.")
            time.sleep(1)


def erro_numeros(mensagem='Digite apenas números: '):
    while True:
        nm = input(mensagem).strip()
        try:
            return int(nm)
        except ValueError:
            print(f"Erro: '{nm}' é inválido! Digite apenas números.")
            time.sleep(1)
def sair ():
    input("\nPressione Enter para voltar ao menu...")
    limpa_tela()


while True:
    
    limpa_tela()
    menu()
    opençao = erro_numeros("Escolha uma opção (1 a 4): ")

    if opençao ==1:
        limpa_tela()
        print('===adicionar produto===')
        
        nome_item = erro_letras()
        quantidade_item = erro_numeros('Digite a quantidade:')
        Preço_item= erro_preco()
                
        item.append(nome_item)
        quantidade.append(quantidade_item)
        Preço.append(Preço_item)
        print(f"\nItem '{nome_item}' adicionado com sucesso| Quantidade: {quantidade_item} | R$:{Preço_item}")
        time.sleep(0.5)
        sair()

    elif opençao == 2:
        limpa_tela()
        print("=== Estoque Atual ===")
        if not item:
            print("O estoque está vazio.")
        else:
            for i in range(len(item)):
                print(f"Item: {item[i]} | Quantidade: {quantidade[i]} | RS:{Preço[i]}")
                time.sleep(1)
                sair() 
    elif opençao == 3:
        limpa_tela()
        print('=== Buscar produto ===')
        nome_item = erro_letras()
        if not item:
            print("O estoque está vazio. Nenhum item para encontrado")
        elif nome_item in item:
            print('===Item encontrado===')
            for i in range(len(item)):
                print(f"Item: {item[i]}")
                time.sleep(1)
                sair() 
        
        else:
            print(f"\nItem '{nome_item}' não encontrado no estoque.")
            time.sleep(1)

    elif opençao == 4:
        limpa_tela()
        print("=== Remover Item do Estoque ===")
        print(f"Itens disponíveis no estoque:{', '.join(item)}")
        nome_item = erro_letras()
        if nome_item in item:
            index = item.index(nome_item)
            del item[index]
            del quantidade[index]
            del Preço[index]
            print(f"\nItem '{nome_item}' removido com sucesso!")
        elif not item:
            print("O estoque está vazio. Nenhum item para remover.")
        else:
            print(f"\nItem '{nome_item}' não encontrado no estoque.")
        time.sleep(1)
    elif opençao == 5:
        print("Saindo do programa...")
        time.sleep(1)
        break
    else:
        print("Opção inválida! Tente novamente.")
        time.sleep(1)
