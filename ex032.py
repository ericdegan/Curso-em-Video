a = int(input('Diga o Ano que quer consultar: '))
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print('o Ano é bissexto')
else:
    print('não é bissexto')