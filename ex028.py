import random

a = random.randint(0,5)
e = int(input('De 0 á 5 qual numero o computador escolheu: '))

if e == a:
     print('O numero sorteado foi', a)
     print("Você VENCEU!!")

else:
    print('O numero sorteado foi', a)
    print('Perdeu OTARIO, me passa um dolar!')

