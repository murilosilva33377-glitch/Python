# Cada linha representa um aluno. Cada coluna é uma nota.
notas = [
    [8.5, 9.0],  # Aluno 0
    [7.0, 6.5],  # Aluno 1
    [10.0, 9.5]  # Aluno 2
]

# Como acessar a primeira nota do Aluno 2 (10.0):
print("Nota isolada:", notas[2][0])  # Linha índice 2, Coluna índice 0
print("-" * 20)

# CORREÇÃO: Adicionada a vírgula faltante no final da primeira linha interna
matriz = [
    [7.0, 6.5, 4.5],  
    [10.0, 9.5, 2.5]
]

# O primeiro loop pega cada linha inteira
for linha in matriz:
    # CORREÇÃO: O segundo loop deve rodar dentro da 'linha', não da 'matriz'
    for elemento in linha:
        print(elemento, end=" ")
    print()  # Pula uma linha no terminal após terminar a linha da matriz

matriz = [  
    [7.0, 6.5, 4.5],  
    [10.0, 9.5, 2.5]
]

# Loop para calcular a soma de cada linha
for i, linha in enumerate(matriz):
    soma_linha = sum(linha)
    print(f"Soma dos elementos da Linha {i}: {soma_linha}")

soma=matriz[0][0]+matriz[0][1]+matriz[0][2]
print(f"Soma dos elementos da Linha 0: {soma}")

import numpy as np

matriz = np.array([
    [10, 20, 30],
    [40, 55, 12]
])

# Encontra o maior valor diretamente
maior_valor = np.max(matriz)

# Encontra a posição (linha, coluna) do maior valor
linha_maior, coluna_maior = np.unravel_index(np.argmax(matriz), matriz.shape)

print(f"Maior valor: {maior_valor}")
print(f"Posição: Linha {linha_maior}, Coluna {coluna_maior}")
