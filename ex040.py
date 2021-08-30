n1 = float(input('\033[4;33mQual a primeira nota\033[m: '))
n2 = float(input('\033[4;33mQual a segunda nota\033[m: '))

m = (n1 + n2) / 2

print('Sua média é {}' .format(m))

if m <= 4.9:
    print('\033[1;31mVocê foi reprovado, estude mais.')
elif m <= 6.9:
    print('\033[1;32mVocê esta de recuperação.')
else:
    print('\033[1;34mVocê foi aprovado, parabens!')