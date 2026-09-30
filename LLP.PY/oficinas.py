import os
import time

aluno = []
oficina_valida = ['Python', 'Robótica', 'Desenvolvimento web']
def limpa_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def erro_letras(men='Digite o nome do aluno: '):
    while True:
        nome = input(men).strip().lower()
        if nome.replace(" ", "").isalpha() and nome != "":
            return nome
        else:
            print(f"Erro: '{nome}' é inválido! Digite apenas letras.")
            time.sleep(1)

def erro_numeros(mensagem='Digite opção : '):
    while True:
        nm = input(mensagem).strip()
        try:
            return int(nm)
        except ValueError:
            print(f"Erro: '{nm}' é inválido! Digite apenas números.")
            time.sleep(1)

def sair():
    input("\nPressione Enter para voltar ao menu...")
    limpa_tela()

def menu():
    print('=-'* 35)
    print('=== INSCRIÇÃO EM OFICINAS ===')
    print('=-'* 35)
    print('''    
    [1]-Realizar inscrição  
    [2]-Lista de inscrição
    [3]-Busca de aluno
    [4]-Cancela inscrição
    [5]-Mostrar total de inscritos
    [6]-Sair''')

def obter_oficina():
    while True:
        oficinas = input(f"Escolha a oficina {oficina_valida}: ").strip().lower()
        for opc in oficina_valida:
            if opc.lower().startswith(oficinas) and oficinas != "":
                return opc 
        print("Erro: Oficina inválida!")
        time.sleep(1)

while True:
    limpa_tela()
    menu()
    opcao = erro_numeros("Escolha uma opção (1 a 6): ") 
    if opcao == 1:
        limpa_tela()
        print('=== REALIZAR INSCRIÇÃO ===')
        nome_aluno = erro_letras()
        oficina_escolhida = obter_oficina()
        aluno.append({"nome": nome_aluno, "oficina": oficina_escolhida})
        print(f"\nSucesso! {nome_aluno.title()} inscrito em {oficina_escolhida}!")
        sair()
        
    elif opcao == 2:
        limpa_tela()
        print('=== Lista de inscrição ===')
        if not aluno:
            print('Lista está vazia.')
        else:
            print('=== Lista de alunos ===')
            for registro in aluno:
                print(f"Aluno: {registro['nome'].title()} | Oficina: {registro['oficina']}")
        sair()
        
    elif opcao == 3:
        limpa_tela()
        print('=== Busca de aluno ===')
        if not aluno:
            print('A lista está vazia. Nenhum aluno encontrado.')
        else:
            nome_buscado = erro_letras("Digite o nome do aluno que deseja buscar: ")
            encontrado = False
            
            for registro in aluno:
                if registro['nome'] == nome_buscado:
                    if not encontrado:
                        print('\n=== Aluno encontrado ===')
                        encontrado = True
                    print(f"Aluno: {registro['nome'].title()} | Curso: {registro['oficina']}")
            
            if not encontrado:
                print(f"\nAluno '{nome_buscado.title()}' não encontrado na lista.")
        sair()
        
    elif opcao == 4:
        limpa_tela()
        print('=== CANCELA INSCRIÇÃO ===')
        if not aluno:
            print('A lista está vazia.')
        else:
            nome_cancela = erro_letras("Digite o nome do aluno para cancelar: ")
            encontrado = False
            for registro in aluno[:]:
                if registro['nome'] == nome_cancela:
                    aluno.remove(registro)
                    print(f"\nInscrição de {nome_cancela.title()} cancelada com sucesso!")
                    encontrado = True
            if not encontrado:
                print(f"\nAluno '{nome_cancela.title()}' não encontrado.")
        sair() 
        
    elif opcao == 5:
        limpa_tela()
        print('=== TOTAL DE INSCRITOS ===')
        print(f"Total de alunos inscritos no sistema: {len(aluno)}")
        sair()
        
    elif opcao == 6:
        limpa_tela()
        print("Saindo do sistema... Obrigado!")
        time.sleep(1)
        break
    else:
        print("Opção inválida! Escolha um número de 1 a 6.")
        time.sleep(1)
