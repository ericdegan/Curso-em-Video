"""c = 0
num = int(input('Digite um numero: '))
cnt = input('Quer continuar [s/n]: ').upper()
media = 0
quantm = 0
maiornum = 0
menornum = num
while c < 1:
    if cnt == 'S' or cnt == 's':
        num = int(input('Digite um numero: '))
        media += num
        quantm += 1
        if num <= menornum:
            menornum = num
        if num >= maiornum:
            maiornum = num
        cnt = input('Quer continuar [s/n]: ').upper()
    elif cnt == 'N':
        print('OK')
        c += 1
    else:
        print('Resposta invalida.')
        cnt = input('Quer continuar [s/n]: ')
media1 = media / quantm
print('Você digitou {} números, e a media deles é {:.0f}'.format(quantm, media1))
print('O maior numero é {}'.format(maiornum))
print(menornum)"""

######################## RESP DO PROFESSOR ###########################

resp = 'S'
soma = quant =  media = 0

while resp in 'Ss':
    num = int(input('digite um numero: '))
    soma += num
    quant +=1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]
media = soma / quant
print('Você digitou {} numeros e a media foi {}'.format(quant,media))
print('O maior numero digitado foi {} e o menor foi {}'.format(maior,menor))