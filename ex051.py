print('-=-'*5,'Vamos Fazer uma PA','-=-'*5)

a = int(input('Escrava o primeiro termo: '))
b = int(input('Escreva agora a RAZAO: '))
d = a + (10 - 1) * b #essa formula é usada para descobrir o decimo termo da PA se eu quisesse o vigezimo termo seria:
# a + (20-1) * b

for c in range(a,d+ 1,b):
    print('{}'.format(c))


print('Esta ai a nossa PA')