dias = int(input('Quantos dias você ficou com o carro? '))
km = float(input('Quantos KM você rodou? '))

#d = dias * 60
#k = km * 0.15
#rs = d + k
rs = (dias * 60) + (km * 0.15)
pc = (rs/100) * 7
dc = rs - pc

print('O valor a pagar será de R$:{:.2f}'.format(rs))
print('Com o desconto de 7% do nosso cartão vai ficar R$:{:.2f}'.format(dc))
print('Você vai economizar R$:{:.2f}'.format(pc))