nome=input('Qual seu nome:')
nota1=float(input('Primeira nota:'))
nota2=float(input('Segunda nota:'))
nota3=float(input('Terceira nota:'))
nota4=float(input('Quarta nota:'))
media=(nota1+nota2+nota3+nota4)/4
print(f'A media da sua nota é {media:.1f}')

if media>= 7:
    print(f'Sua nota foi aprovado {nome}')
elif media <= 4:
    print(f'Você está de recuperasão {nome}')
else:
    print(f'Sua nota foi reprovado {nome}')
