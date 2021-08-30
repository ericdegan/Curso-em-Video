c = 0
soma = 0
qnt = 0
while c < 1:
    a = int(input('Escreva um numero: '))
    print('Se quiser parar digite [999]')
    soma += a
    qnt += 1
    if a == 999:
        c += 1
        qnt -= 1
print('Você digitou {} números, a soma dessa numero é {}.'.format(qnt, soma - 999))



#################CODIGO DO PROFESSOR################
""" 
num = cont = soma = 0
num = int(input('Digite um numero [999 para parar]:'))
while num != 999:
    soma += num
    cont += +1
    num = int(input('Digite um numero [999 para parar]:')) 
print('Você digitou {} numeros e a soma entre eles foi {}'.format(cont, soma))"""