valor = float(input('Qual o valor a pagar R$:'))
pag = input('Você pode pagar em [1] Dinheiro ou [2] Cartão qual você prefere? ').upper()

if pag == ('1'):
    print('Em dinheiro você ganha 10% de desconto vai ficar R$:{:.2f}'.format(valor - (valor/100) * 10))
elif pag == ('2'):
    cart = input('Voce quer pagar á [1] vista, em [2] 2x ou [3] 3x no cartão? ')
    if cart == '2':
        print('Em duas vezes o vai ficar R$:{:.2f} por mês'.format(valor/2))
    elif cart == '3':
        juros = (valor/100) * 20
        print('Em três vezes vai ficar R${:.2f} por mês'.format(valor/3 + juros))
    else:
        desc = (valor/100) * 5
        print('A vista no cartão temos 5% de desconto, vai ficar R$:{:.2f}'.format(valor - desc))
