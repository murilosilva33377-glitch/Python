import os
import time


nomes = []
quantidades = []
precos = []
produto=[]

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def pausa():
    input("\nPressione Enter para voltar ao menu... ")
    limpar_tela()

def menu():
    print("="*40)
    print(" CANTINA DA ESCOLA")
    print("="*40)
    print('''
    1 - Adicionar produto à compra
    2 - Ver produtos da compra
    3 - Remover produto da compra
    4 - Finalizar compra e emitir nota fiscal
    5 - Sair''')
    print("="*40)

def erro_letra(msg):
    while True:
        texto = input(msg).strip()
        if texto.replace(" ", "").isalpha() and texto!= "":
            return texto
        else:
            print(f"Erro: Digite apenas letras.")
            time.sleep(1)

def erro_int(msg):
    while True:
        try:
            valor = int(input(msg).strip())
            if valor <= 0:
                print("Erro: O valor deve ser maior que zero!")
                time.sleep(1)
                
            return valor
        except ValueError:
            print("Erro: Digite um número inteiro válido!")
            time.sleep(1)

def erro_float(msg):
    while True:
        try:
            valor = float(input(msg).strip().replace(',', '.'))
            if valor <= 0:
                print("Erro: O valor deve ser maior que zero!")
                time.sleep(1)
            return valor
        except ValueError:
            print("Erro: Digite um preço válido!")
            time.sleep(1)


while True:
    limpar_tela()
    menu()
    opcao = erro_int("Escolha uma opção (1 a 4): ")

    if opcao == 1:
        limpar_tela()
        print("=== Adicionar produto à compra ===\n")
        prod = erro_letra('Digite o nome do produto: ')
        qtd = erro_int('Digite a quantidade: ')
        prc = erro_float('Digite o preço R$: ')

        nomes.append(prod)
        quantidades.append(qtd)
        precos.append(prc)

        print(f"\nItem '{prod.title()}' adicionado! Qtd: {qtd} | R${prc:.2f}")
        pausa()

    elif opcao == 2:
        limpar_tela()
        print("=== Produtos da compra ===\n")
        if not nomes:
            print('A compra está vazia.')
        else:
            for i in range(len(nomes)):
                subtotal = quantidades[i] * precos[i]
                print(f"{i+1}. {nomes[i].title()} | Qtd: {quantidades[i]} | R$ {precos[i]:.2f} | Sub: R$ {subtotal:.2f}")
        pausa()

    elif opcao == 3:
        limpar_tela()
        print("=== Remover produto da compra ===")
        if not nomes:
            print('A compra está vazia, nada para remover.')
        else:
    #
            for i in range(len(nomes)):
                print(f"{i+1} - {nomes[i].title()}")

            indice = erro_int('\nDigite o número do produto que quer remover: ')
            if 1 <= indice <= len(nomes):
                removido = nomes.pop(indice-1)
                quantidades.pop(indice-1)
                precos.pop(indice-1)
                print(f"\n'{removido.title()}' removido com sucesso!")
            else:
                print("\nErro: Número inválido!")
        pausa()

    elif opcao == 4:
        limpar_tela()
        if not nomes:
            print("ERRO: Não é possível emitir nota com a compra vazia!")
            print("Adicione produtos primeiro.")
            pausa()
           
        print("="*52)
        print(" NOTA FISCAL — CANTINA")
        print("="*52)
        cliente_nome = erro_letra('Digite o nome do cliente: ')
        print(f"Cliente: {cliente_nome.title()}\n")
        print(f"{'Produto':<15} {'Qtd.':<5} {'Preço un.':<12} {'Subtotal'}")
        print("-"*52)

        total = 0
        for i in range(len(nomes)):
            subtotal = quantidades[i] * precos[i]
            total += subtotal
            print(f"{nomes[i].title():<15} {quantidades[i]:<5} R$ {precos[i]:<8.2f} R$ {subtotal:.2f}")

        print("-"*52)
        print(f"TOTAL A PAGAR: R$ {total:.2f}")
        print("="*52)

        resp = input("\nDeseja iniciar uma nova compra? (S/N): ").strip().lower()
        if resp == 's':
            nomes.clear()
            quantidades.clear()
            precos.clear()
            print("\nNova compra iniciada!")
            time.sleep(1)
            limpar_tela()
        else:
            print("\nEncerrando sistema... Obrigado!")
            break

    elif opcao == 5:
        limpar_tela()
        print("Saindo do sistema... Até logo!")
        break
    else:
        print("Opção inválida! Tente novamente.")
        time.sleep(1)