t=0
numeros_extenso = (
    "zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", 
    "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", 
    "dezessete", "dezoito", "dezenove", "vinte"
)
while True:
    num = int(input("Digite um número entre 0 e 20: "))
    if 0 <= num <= 20:
        print(f"Você digitou o número {numeros_extenso[num]}.")
        break
    else:
        print("Número inválido. Tente novamente.")
    t+=1
print(f'Você tentou {t} vezes até acertar.')