from math import factorial
n = int(input('Digite um numero para calcular seu fatorial: '))
fac = factorial(n)
print('O fatorial de {} é {}'.format(n, fac))

######################### segunda formula #####################

n = int(input('Digite um numero para calcular seu fatorial: '))
c = n
f = 1
print('Calculando fatorial de {}'.format(n))
while c > 0:
     print('{}'.format(c), end=' ')
     print('x' if c > 1 else ' = ', end= ' ')
     f *= c
     c -= 1

print(f)