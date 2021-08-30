n1 = int(input('Um numero:'))
n2 = int(input('Outro numero'))
s = n1 + n2
ss = n1 + n2 + 1
si = n1 + n2 - 1
print('A soma é igual á: {} \n Seu sucessor é: {} \n Seu antecessor é: {}'.format(s, ss, si))
#Poderia ter formatado assim .format(s, s+1, s-1)

n3 = int(input('um numero'))
print('Sucessor:{} , Antecessor:{}'.format((n3+1), (n3-1)))