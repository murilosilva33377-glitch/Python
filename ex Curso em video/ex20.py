import random
nm1=input ('primeiro aluno:')
nm2=input('segundo aluno:')
nm3=input("Terceiro aluno:")
nm4=input('Quarto aluno:')
nm=[nm1,nm2,nm3,nm4]
random.shuffle(nm)
print(f' Parabéns você foi escolhido!!!\n{nm}')
