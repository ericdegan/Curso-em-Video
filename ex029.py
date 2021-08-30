v = int(input('Você veio a quantos km/h? '))
m = float(v - 80) * 7

if v >= 81:
    print('Voce veio á {}? Você concerteza foi multado.'.format(v))
    print('A essa velocidade a multa vai ser de R$:{:.2f}'.format(m))
if v == 80:
    print('Se passasse um pouco mais que isso tomaria um multa.')
if v <= 79:
    print('Ta tranquilo os radares até aqui são de 80km/h')

