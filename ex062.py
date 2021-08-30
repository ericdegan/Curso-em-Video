pt = int(input('Diga o primeiro termo: '))
rz = int(input('Diga a razao: '))
d = pt + (10 - 1) * rz
pa = 0
c = 1
z = 1
while c < 11:
    f = pa + pt
    pa += rz
    print(f)
    c += 1
    if c == 11:
        prox = int(input('Você gostaria de ver mais quantos termos: '))

        if prox != 0:
            while z < prox +1:
                f = pa + pt
                pa += rz
                print(f)
                z += 1


        else:
            print('Tudo bem, terminamos aqui.')



