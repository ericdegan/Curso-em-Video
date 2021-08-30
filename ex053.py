a = str(input('Escreva uma frase: ')).strip().upper()
frase = a.split()
junto = ''.join(frase)
inv = ''
for plv in range(len(junto) - 1, -1, -1):
       inv += junto[plv]
if inv == junto:
    print('Essa frase é um palídromo!')
else:
    print('Essa frase não é um palídromo!')


print(inv,junto)

