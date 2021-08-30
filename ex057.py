sexo = 0
while sexo != 'F' and sexo != 'M':
    sexo = str(input('Por favor digite seu sexo [M/F]: ')).upper()
    if sexo == 'M':
        print('Você é do sexo Masculino')
    elif sexo == 'F':
        print('Você é do sexo Feminino')
    else:
        print('Isso não é um sexo')