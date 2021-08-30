d = int(input('Quantos KM tem nessa viagem? '))

print('Hmm {}KM'.format(d))
if d <= 200:
    print('O valor dessa viagem sera R$:{:.2f}'.format(float(d*0.50)))
else:
    print('O valor dessa viagem vai ser RS:{:.2f}'.format(float(d*0.45)))
