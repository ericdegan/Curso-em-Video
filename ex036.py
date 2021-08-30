print('Olá quero comprar uma casa,você pode me ajudar?')
from time import sleep
sleep(1)
print('Claro que posso, só preciso saber algumas informações')
sleep(2)

valor = int(input('Qual o valor da casa: '))
sal = int(input('Quanto você recebe de salario: '))
anos = int(input('Em quantos anos você quer pagar: '))

prestacao = valor / anos
aprov = (prestacao / 12 <= sal/100 * 30)

if aprov == (True):
   print('Eu posso financiar está casa para você, a vai sair \033[1;32m {:.2f} \033[m por mês'.format(prestacao/12))
else:
   print('Me desculpe, mas não podemos financiar esta casa para você. \033[1;31m POBRE FILHO DA PUTA!')

