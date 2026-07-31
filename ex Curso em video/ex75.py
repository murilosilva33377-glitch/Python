n1=int(input('Digete um numero: '))
n2=int(input('Digete outro numero: '))
n3=int(input('Digete mais um numero: '))
n4=int(input('Digete o ultimo numero: '))
nt=(n1, n2, n3, n4)
print(f'você digitou os numeros: {nt}')
print(f'o numero 9 apareceu {nt.count(9)} vezes')
print(f'o numero 3 apareceu na posição {nt.index(3)+1}ª' if 3 in nt else 'o numero 3 não foi digitado')
for n in nt:
    if n % 2 == 0:
        print(f'os numeros pares digitados foram: {n}')
