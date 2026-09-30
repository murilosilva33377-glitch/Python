print('__'*10)
peso=float(input('Qual seu peso:'))
altura=float(input('Qual sua altura:'))
print('__'*10)
imc=peso/(altura*altura)
print(f' Seu imc é {imc:.2f}')
if imc<18.5:
    print('Abaixo do peso')
elif imc>=18.5 and imc<25:
    print('Peso normal')
elif imc>=25 and imc<30:
    print('Sobrepeso')
elif imc>=30 and imc<35:
    print('Obesidade')
elif imc>=35 and imc<40:
    print('Obesidade2')
else:
    print('Obesidade 3')