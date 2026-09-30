viagem = []
pessoa = []
pessoamax = []

def cadastro_voo():
    
    print('=' * 40)
    print('             CONTROLE DE VOO PYTHON             ')
    print('=' * 40)    
    for i in range(5):
        print(f'\n[ Cadastro do Voo {i + 1} ]')
        
        while True:
            empresa = input('Código do voo (Latam ou Azul): ').strip()
           
            if empresa.lower().startswith('latam') or empresa.lower().startswith('azul'):
                break
            print(f"Erro: '{empresa}' é inválido! O código deve iniciar com 'Latam' ou 'Azul'.")
        
        
        while True:
            passageiro = input('Passageiros confirmados: ').strip()
            try:
                passageiro_int = int(passageiro)  
                break  
            except ValueError:
                print(f"Erro: '{passageiro}' é inválido! Digite apenas números.")
        
       
        while True:
            max_passageiros = input('Capacidade máxima: ').strip()
            try:
                max_passageiros_int = int(max_passageiros)  
                break  
            except ValueError:
                print(f"Erro: '{max_passageiros}' é inválido! Digite apenas números.")
        viagem.append(empresa.upper())
        pessoa.append(passageiro_int)
        pessoamax.append(max_passageiros_int)

def exibir_relatorios():
   
    print('\n' + '=' * 40)
    print('             RELATÓRIO DE OCUPAÇÃO             ')
    print('=' * 40)
    
    for i in range(5):
        print(f"Voo: {viagem[i]} | Passageiros: {pessoa[i]} | Capacidade: {pessoamax[i]}")
        
    print('\n' + '=' * 40)
    print('          ALERTA DE LOTAÇÃO CRÍTICA          ')
    print('=' * 40)
    
    for i in range(5):
      
        if pessoa[i] >= pessoamax[i]:
            print(f"-> {viagem[i]}")
cadastro_voo()
exibir_relatorios()