pt = int(input('Diga o primeiro termo: '))
rz = int(input('Diga a razao: '))
pa = 0
c = 1
while c < 11:
    f = pa + pt
    pa += rz
    c += 1
    if c > 1:
        print(f)


print('Esta ai nossa PA')