notasala = []
nota = 1
print('=-' * 20)
while True: 
    entrada = input(f'Digite a nota {nota} (ou "Sair" para fechar): ').strip().lower()  
    if entrada == 'sair':
        break
    try:
        valor_nota = float(entrada)
        notasala.append(valor_nota)
        nota += 1
    except ValueError:
        print('Entrada inválida!. Por favor, digite um número ou "Sair".')
print('=-' * 20)
if len(notasala) > 0:
    media = sum(notasala) / len(notasala)
    if media >= 7:
        desempenho = 'satisfatório'
    else:
        desempenho = 'insatisfatório'  
    print(f'Média da turma: {media:.2f}')
    print(f'Status: Desempenho {desempenho}.')
else:
    print('Nenhuma nota foi registrada.')       