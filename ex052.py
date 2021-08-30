a = int(input('Digite um numero: '))
div = 0
for c in range(1,a + 1):
    if a % c == 0:
        print('\033[34m', end = ' ')
        div += 1
    else:
        print('\033[m' , end = ' ')
    print('{}'.format(c), end = ' ')

print('O numero {} foi divisivel {} vezes'.format(a, div))
if div == 2:
    print('Podemos dizer que o numero {} é um numero primo'.format(a))
else:
    print(' {} não é um numero primo'.format(a))



