maior = 0
menor = 0

for c in range(1,6):
    pesoum = float(input('{}º peso: '.format(c)))
    if c == 1:
        maior = pesoum
        menor = pesoum
    else:
        if pesoum > maior:
            maior = pesoum
        if pesoum < menor:
            menor = pesoum

print('O maior peso foi {}'.format(maior))
print('O menor peso foi {}'.format(menor))
