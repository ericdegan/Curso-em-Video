from random import randint
print('Vamos jogar par ou impar')
vit = 0
while True:
    esc = int(input('Qual você escolhe [1] PAR  ou [2] IMPAR]: '))
    p1 = int(input('Que numero você vai jogar: '))
    p2 = randint(1,10)
    result = (p1 + p2) % 2
    if esc == 1:
        print('Você escolheu Par')
        if result == 0:
            print(f'Você escolheu numero {p1} e o computador numero {p2}')
            print('Você venceu')
            vit += 1
        else:
            print(f'Você escolheu numero {p1} e o computador numero {p2}')
            print('Você Perdeu')
            break
    elif esc == 2:
        print('Você escolheu Impar')
        if result == 1:
            print(f'Você escolheu numero {p1} e o computador numero {p2}')
            print('Você Venceu')
            vit += 1
        else:
            print(f'Você escolheu numero {p1} e o computador numero {p2}')
            print('Você perdeu')
            break
print(f'Você conseguil vencer {vit} vezes consecutivas')