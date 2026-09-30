import os
import time

nomes = []
quantidades = []
precos = [] 

cantina_precos = {
    "Pão de queijo": 4.50,
    "Salgados assados": 6.00,
    "Sanduíche natural": 8.50,
    "Suco natural": 5.00,
    "Salada de frutas": 7.00
}

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def pausa():
    input("\nPressione Enter para voltar ao menu... ")
    limpar_tela()

def menu():
    print("="*40)
    print(" CANTINA DA ESCOLA".center(40))
    print("="*40)
    print("1 - Adicionar produto à compra")
    print("2 - Ver produtos da compra")
    print("3 - Remover produto da compra")
    print("4 - Finalizar compra e emitir nota fiscal")
    print("5 - Sair")
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

def escolha_produto():
    print("--- CARDÁPIO ---")
    for i, (produto, preco) in enumerate(cantina_precos.items(), 1):
        print(f"{i} - {produto} - R$ {preco:.2f}")
    print("----------------")

    while True:
        digito = input("Digite o nome ou número do produto: ").strip().lower()

        
        if digito.isdigit():
            idx = int(digito) - 1
            if 0 <= idx < len(cantina_precos):
                nome_produto = list(cantina_precos.keys())[idx]
                return nome_produto

        for nome_completo in cantina_precos:
            if nome_completo.lower().startswith(digito) and digito!= "":
                return nome_completo

        print("Erro: Produto inválido! Tente novamente.")
        time.sleep(1)


while True:
    limpar_tela()
    menu()
    opcao = erro_int("Escolha uma opção (1 a 5): ")

    if opcao == 1:
        limpar_tela()
        print("=== Adicionar produto à compra ===\n")
        nome_escolhido = escolha_produto()
        qtd = erro_int('Digite a quantidade: ')

        preco_unitario = cantina_precos[nome_escolhido]

        nomes.append(nome_escolhido)
        quantidades.append(qtd)
        precos.append(preco_unitario)

        print(f"\nItem '{nome_escolhido}' adicionado! Qtd: {qtd} | R$ {preco_unitario:.2f}")
        pausa()

    elif opcao == 2:
        limpar_tela()
        print("=== Produtos da compra ===\n")
        if not nomes:
            print('A compra está vazia.')
        else:
            for i in range(len(nomes)):
                subtotal = quantidades[i] * precos[i]
                print(f"{i+1}. {nomes[i]} | Qtd: {quantidades[i]} | R$ {precos[i]:.2f} | Sub: R$ {subtotal:.2f}")
        pausa()

    elif opcao == 3:
        limpar_tela()
        print("=== Remover produto da compra ===\n")
        if not nomes:
            print('A compra está vazia, nada para remover.')
        else:
            for i in range(len(nomes)):
                print(f"{i+1} - {nomes[i]}")
            indice = erro_int('\nDigite o número do produto que quer remover: ')
            if 1 <= indice <= len(nomes):
                removido = nomes.pop(indice-1)
                quantidades.pop(indice-1)
                precos.pop(indice-1)
                print(f"\n'{removido}' removido com sucesso!")
            else:
                print("\nErro: Número inválido!")
        pausa()

    elif opcao == 4:
        limpar_tela()
        if not nomes:
            print("ERRO: Não é possível emitir nota com a compra vazia!")
            print("Adicione produtos primeiro.")
            pausa()
            

        print("="*56)
        print(" NOTA FISCAL — CANTINA".center(56))
        print("="*56)
        cliente_nome = erro_letra('Digite o nome do cliente: ')
        print(f"Cliente: {cliente_nome.title()}\n")
        print(f"{'Produto':<20} {'Qtd.':<5} {'Preço un.':<12} {'Subtotal'}")
        print("-"*56)

        total = 0
        for i in range(len(nomes)):
            subtotal = quantidades[i] * precos[i]
            total += subtotal
            print(f"{nomes[i]:<20} {quantidades[i]:<5} R$ {precos[i]:<8.2f} R$ {subtotal:.2f}")

        print("-"*56)
        print(f"TOTAL A PAGAR: R$ {total:.2f}")
        print("="*56)

        resp = input("\nDeseja iniciar uma nova compra? (S/N): ").strip().lower()
        if resp == 's':
            nomes.clear()
            quantidades.clear()
            precos.clear()
            print("\nNova compra iniciada!")
            time.sleep(1)
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
