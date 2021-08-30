n = float(input('Qual o preço do produto? R$:'))

s = n / 100 *5
d = n - s

print('Com o desconto de 5% fica R$:{:.2f}'.format(d))
print('Você vai economizar R$:{:.2f}'.format(s))