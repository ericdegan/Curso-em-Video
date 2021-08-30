from datetime import date
div = 0
dive = 0

for d in range(1,8):
   ano = int(input('Em que ano a {}ª pessoa nasceu: '.format(d)))
   atual = date.today().year
   dif = atual - ano
   if dif > 17:
      div += +1
   elif dif < 18:
      dive += +1
print('Existem {} maiores e idade e {} menores de idade'.format(div,dive))
