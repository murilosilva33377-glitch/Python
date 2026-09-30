import os
import time

def limpa_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def sair():
    input("\nPressione Enter para continuar...")
    limpa_tela()

def erro_numeros(mensagem='Digite apenas números: '):
    while True:
        nm = input(mensagem).strip().replace(",", ".")
        try:
            return float(nm)
        except ValueError:
            print(f"Erro: '{nm}' é inválido! Digite apenas números.")
            time.sleep(1)


limpa_tela()
print('=-' * 35)
print("=== MONITORAMENTO DE VENDAS ===")
print('=-' * 35)


matriz = [[0]*4 for _ in range(4)]
soma = 0
maior = 0
linha_maior = 0
coluna_maior = 0


for i in range(4): 
    for j in range(4): 
        valor = erro_numeros(f"Digite o faturamento da filial [{i}] dia [{j}]: R$ ")
        matriz[i][j] = valor
        soma += valor
        limpa_tela()

        if i == 0 and j == 0:
            maior = valor
        elif valor > maior:
            maior = valor
            linha_maior = i
            coluna_maior = j
            

print('=-' * 35)
print("=== MAPA FINANCEIRO DA REDE ===")
print('=-' * 35)

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(f"[ {matriz[i][j]} ]", end=" ")
    print()

print('=-' * 35)
print("=== RELATÓRIO DE ANÁLISE ===")
print('=-' * 35)

media = soma / 16

print(f"Média geral da rede: {media} R$")
print(f"Maior faturamento: {maior} R$ na posição Linha {linha_maior}, Coluna {coluna_maior}")
print('=-' * 35)

sair()