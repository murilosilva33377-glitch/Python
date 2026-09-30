vendas = [
    [1200, 1500, 1100],
    [1000, 1300, 1400],
    [900, 1700, 1600]
]

print('=-' * 20)
print(f"{'Vendas por venda':^10}")
print('=-' * 20)
for linha in vendas:
    print(linha)
print('=-' * 20)
print(f"{'Total por vendedor':^10}")
print('=-' * 20)

vendor =0
for linha in vendas:
    total_vendedor =0
    for venda in linha:
        total_vendedor += venda
    print(f"Vendedor {vendor}: Total de vendas = {total_vendedor}")
    vendor += 1

print('=-' * 20)
print(f"{'Total por mês':^10}")
print('=-' * 20)

for coluna in range(3): 
    total_mes = 0
    for linha in vendas:
        total_mes += linha[coluna]
    print(f"Mês {coluna}: Total de vendas = {total_mes}")

print('=-' * 20)
print(f"{'Total Geral':^10}")
print('=-' * 20)

totalgeral=0
for linha in vendas:
    for valor in linha:
        totalgeral += valor
print('Total Geral de vendas =', totalgeral)

print('=-' * 20)
print('Melhor vendedor:')
print('=-' * 20)
melhor_vendedor = 0
melhor_total = 0
vendedor = 0

for linha in vendas:
    total_vendedor = 0
    for venda in linha:
        total_vendedor += venda
    if total_vendedor > melhor_total:
        melhor_total = total_vendedor
    vendor += 1
print(f"Vendedor {melhor_vendedor}\ncom total de vendas = {melhor_total}")