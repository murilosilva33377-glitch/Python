#Código 1: Apenas Números (EUA try/except)
while True:
    nm = input('Digite apenas números: ').strip()
    try:
        int(nm) # Se tiver letras, dá erro e vai para o except
        break
    except ValueError:
        print(f"Erro: '{nm}' é inválido! Digite apenas números.")

print(f"Número invertido: {nm[::-1]}")
#Código 2: Apenas Letras (Sem try, usando apenas if)
while True:
    nome = input('Digite apenas letras/nome: ').strip()
    
    if nome.isalpha(): # Se for apenas letras, o programa aceita
        break
    else:
        print(f"Erro: '{nome}' é inválido! Digite apenas letras.")

print(f"Nome invertido: {nome[::-1]}")
