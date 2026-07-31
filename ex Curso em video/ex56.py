mih=0
somaidade=0
nomev=''
totm=0
mid=0
for c in range(1,5):
     print(f'------{c}pessoa------')
     nm=str(input('Qual seu nome:')).strip()
     id=int(input('Qual seu idade:'))
     gn=str(input('[H/M]:')).strip()
     somaidade+= id
     if c==1 and gn in'H':
         mih=id
         nomev=nm
     if gn in 'H' and id>mih:
          mih=id
          nomev=id
     if gn in 'M' and id<20:
          totm+=1
md=somaidade/4
print(f'A média  do grupo é de{mid} anos')
print(f'O homem mais velhor tem {mih} anos e se chama {nomev}')
print(f'Quantidade de {totm} Mulher com menos de {mid}')