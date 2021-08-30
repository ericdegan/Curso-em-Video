from random import randint
tentativas = 0
a = randint(1,10)
e = 0
print('*-*'*5, '!JOGO DO ADVINHA!', '*-*'*5)
print('Estou pensando em um numero de 0 a 10, tente advinhar qual é!')
e = int(input('Diga um numero: '))
while e != a:
    print('Não, tente denovo')
    e = int(input('Diga um numero: '))
    tentativas += 1

print('Acertou, você só precisou de {} palpites'.format(tentativas +1))