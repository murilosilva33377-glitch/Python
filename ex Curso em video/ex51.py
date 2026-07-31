p=int(input('primero termo:'))
r=int(input('razão:'))
d=p+(10-1)*r
for c in range(p,d,r):
    print(f'{c}',end=' >')
print('acabou')