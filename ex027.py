n = str(input('Escreva seu nome completo: ')).strip().title()
nome = n.split()

print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu ultimo nome é {}'.format(nome[len(nome)-1]))
#QUANDO VOCE PÕE UM -1 JUNTO COM O COMANDO LEN ELE LE O ULTIMO SPLIT
