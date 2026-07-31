print('Qual sua velocida?')
km=float(input('km:'))
if km>80:
     print('MULTADO!!!\n Você passou limete da velocidade de 80Km/h')
     print(f'Multa custa R${(km-80)*7}')
else:
     print('Você está na velocidade correta')

