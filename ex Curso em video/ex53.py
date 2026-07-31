nm=str(input('Digite seu nome:'))
# for c in range(nm,0,-1):
#     print(f'o inverso {nm} é {c}')
nome = []
for c in nm:
    nome.append(c)

nm.reverse()
print(nm)