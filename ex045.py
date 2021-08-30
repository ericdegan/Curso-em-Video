print('='*20)
print('     JOOKEENPO!')
print('='*20)
import random
a = str(input('Pedra, Papel ou Tesoura? ')).upper()
import random
c = ['PEDRA', 'PAPEL', 'TESOURA']
#d = random.randint(0, 2) #Com esse comando eu poderia formatar o print da seguinte forma
b = random.choice(c)  #print('O computador escolheu {}'.format(c[d])) ai eles escolheria o string na posição de 0 á 2
print('Voce escolheu {} e o computador {}.'.format(a, b))
if b == 'PEDRA' and a == 'PAPEL':
    print('\033[34mVOCÊ VENCEU!')
elif b == 'PAPEL' and a == 'TESOURA':
    print('\033[34mVOCÊ VENCEU!')
elif b == 'TESOURA' and a == 'PEDRA':
    print('\033[34mVOCÊ VENCEU!')
elif b == a:
    print('\033[33mEMPATOU!')
    print('Vamos denovo.')
else:
    print('\033[31mVOCÊ PERDEU!')

