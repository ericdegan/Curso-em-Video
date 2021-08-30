print('Analise')
media1 = 0
media2 = 0
media3 = 0
media4 = 0
mv = 0
mulheres = 0
nmv = 0
nome1 = 0
nome2 = 0
nome3 = 0
nome4 = 0

for c in range(1,5):
    print('{}ª Pessoa: '.format(c))
    nome = str(input(' Nome: ')).title()
    idade = int(input(' Idade: '))
    sexo = str(input(' Sexo [M/F]: ')).upper()
    if c == 1:
        media1 = idade
        nome1 = nome
        if sexo == 'F' and media1 < 18:
            mulheres += 1

    if c == 2:
        media2 = idade
        nome2 = nome
        if sexo == 'F'and media2 < 18:
            mulheres += 1
    if c == 3:
        nome2 = nome
        media3 = idade
        if sexo == 'F'and media3 < 18:
            mulheres += 1
    else:
        nome4 = nome
        media4 = idade
        if sexo == 'F' and media4 < 18:
            mulheres += 1
        if media1 > media2 and media1 > media3 and media1 > media4:
            mv = media1
            nmv = nome1
        if media2 > media1 and media2 > media3 and media2 > media4:
            mv = media2
            nmv = nome2
        if media3 > media2 and media3 > media1 and media3 > media4:
            mv = media3
            nmv = nome3
        if media4 > media1 and media4 > media3 and media4 > media2:
            mv = media4
            nmv = nome4

media = (media1 + media2) /2
print('O mais velho deste grupo é o {} e tem {} anos'.format(nmv, mv))
print('A media de idade desse grupo é: {:.0f}'.format(media))
print('Existem {} mulheres menores de idade.'.format(mulheres))
