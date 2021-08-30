mult = 0
print('-'*40)
n = int(input('Qual tabuada você deseja saber: '))
print('-'*40)
while True:
    if n >= 1:
        mult += 1
        result = n * mult
        print(f'{n} * {mult} = \033[1;32m{result}\033[m')
        if mult == 10:
            print('-' * 40)
            print('Digite [0] se deseja encerar o programa')
            print('-' * 40)
            n = int(input('Qual tabuada você deseja saber agora: '))
            print('-' * 40)
            mult -= 10

    else:
        break
print('Programa encerrado')




