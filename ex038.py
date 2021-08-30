n1 = int(input('Escreva um numero: '))
n2 = int(input('Escreva outro numero: '))
from time import sleep
print('PROCESSANDO.')
sleep(.7)
print('PROCESSANDO..')
sleep(.7)
print('PROCESSANDO...')
sleep(.7)
print('PROCESSANDO.')
sleep(.7)
print('PROCESSANDO..')
sleep(.7)
print('PROCESSANDO...')
sleep(.3)
if n1 > n2:
    print('O numero \033[1;33m{}\033[m é o maior'.format(n1))
elif n1 < n2:
    print('O numero \033[1;36m{}\033[m é o maior'.format(n2))
else:
    print('\033[4;32mNão existe numero maior os dois são iguais')
