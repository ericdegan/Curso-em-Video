soma = 0
cont = 0
for c in range(1,7):
   a = int(input('Escreva o {} numero: '.format(c)))
   if a%2 == 0:
      soma += +a
      cont += +1

print('Você somou {} numeros e a soma dos numeros é = {}'.format(cont,soma))








