import os
import time


ARQUIVO_DADOS = "inscritos.txt"
OFICINAS_VALIDAS = ["Python", "Robótica", "Desenvolvimento"]

def limpa_tela():
    os.system("cls" if os.name == "nt" else "clear")


def sair():
    input("\nPressione Enter para voltar ao menu... ")
    limpa_tela()


def menu():
    """Exibe o menu principal no terminal."""
    print("=-" * 35)
    print("=== INSCRIÇÃO EM OFICINAS ===".center(70))
    print("=-" * 35)
    print("[1] - Realizar inscrição")
    print("[2] - Lista de inscrição")
    print("[3] - Busca de aluno")
    print("[4] - Cancela inscrição")
    print("[5] - Mostrar total de inscritos")
    print("[6] - Sair")
    print("-" * 70)


def carregar_dados():
    lista_alunos = []
    if os.path.exists(ARQUIVO_DADOS):
        with open(ARQUIVO_DADOS, "r", encoding="utf-8") as f:
            for linha in f:
                linha = linha.strip()
                if linha and "|" in linha:
                    nome, oficina = linha.split("|")
                    lista_alunos.append({"nome": nome, "oficina": oficina})
    return lista_alunos


def salvar_dados(lista_alunos):
    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as f:
        for reg in lista_alunos:
                f.write(f"{reg['nome']}|{reg['oficina']}\n")



def erro_letras(mensagem="Digite o nome do aluno: "):
    
    while True:
        nome = input(mensagem).strip().lower()
        if nome.replace(" ", "").isalpha() and nome != "":
            return nome
        else:
            print(f"Erro: '{nome}' é inválido! Digite apenas letras.")
            time.sleep(1)


def erro_numeros(mensagem="Digite a opção: "):
    while True:
        nm = input(mensagem).strip()
        try:
            return int(nm)
        except ValueError:
            print(f"Erro: '{nm}' é inválido! Digite apenas números.")
            time.sleep(1)


def obter_oficina():
    while True:
        print("\nOficinas disponíveis:")
        for i, oficina in enumerate(OFICINAS_VALIDAS, 1):
            print(f"{i} - {oficina}")
        

        escolha = input(f"Escolha uma oficina (1 a {len(OFICINAS_VALIDAS)} ou nome): ").strip().lower()
        if escolha.isdigit():
            indice = int(escolha) - 1
            if 0 <= indice < len(OFICINAS_VALIDAS):
                return OFICINAS_VALIDAS[indice]
        for opcao_valida in OFICINAS_VALIDAS:
            if opcao_valida.lower().startswith(escolha) and escolha != "":
                return opcao_valida
                
        print("Erro: Oficina inválida! Escolha pelo número ou digite o nome.")
        time.sleep(1.5)


alunos = carregar_dados()

while True:
    limpa_tela()
    menu()
    opcao = erro_numeros("Escolha uma opção (1 a 6): ")

    if opcao == 1:
        limpa_tela()
        print("=== REALIZAR INSCRIÇÃO ===\n")
        nome_aluno = erro_letras()
        oficina_escolhida = obter_oficina()
        
        alunos.append({"nome": nome_aluno, "oficina": oficina_escolhida})
        salvar_dados(alunos)
        
        print(f"\nSucesso! {nome_aluno.title()} inscrito em {oficina_escolhida}!")
        sair()

    elif opcao == 2:
        limpa_tela()
        print("=== LISTA DE INSCRIÇÃO ===\n")
        if not alunos:
            print("A lista está vazia.")
        else:
            for registro in alunos:
                print(f"Aluno: {registro['nome'].title():<25} | Oficina: {registro['oficina']}")
        sair()

    elif opcao == 3:
        limpa_tela()
        print("=== BUSCA DE ALUNO ===\n")
        if not alunos:
            print("A lista está vazia. Nenhum aluno cadastrado.")
        else:
            nome_buscado = erro_letras("Digite o nome do aluno que deseja procurar: ")
            encontrado = False
            for registro in alunos:
                if registro["nome"] == nome_buscado:
                    if not encontrado:
                        print("\n=== Aluno(s) Encontrado(s) ===")
                        encontrado = True
                    print(f"Aluno: {registro['nome'].title():<25} | Oficina: {registro['oficina']}")
            if not encontrado:
                print(f"\nAluno '{nome_buscado.title()}' não encontrado na lista.")
        sair()

    elif opcao == 4:
        limpa_tela()
        print("=== CANCELA INSCRIÇÃO ===\n")
        if not alunos:
            print("A lista está vazia.")
        else:
            nome_cancela = erro_letras("Digite o nome do aluno para cancelar: ")
            encontrado = False
            
          
            for registro in alunos[:]:
                if registro["nome"] == nome_cancela:
                    alunos.remove(registro)
                    print(f"Inscrição de {nome_cancela.title()} cancelada com sucesso!")
                    encontrado = True
            
            if encontrado:
                salvar_dados(alunos)
            else:
                print(f"\nAluno '{nome_cancela.title()}' não encontrado.")
        sair()

    elif opcao == 5:
        limpa_tela()
        print("=== TOTAL DE INSCRITOS ===\n")
        print(f"Total de alunos inscritos no sistema: {len(alunos)}")
        sair()

    elif opcao == 6:
        limpa_tela()
        print("Saindo do sistema... Obrigado!")
        time.sleep(1)
        break

    else:
        print("Opção inválida! Escolha um número de 1 a 6.")
        time.sleep(1)
