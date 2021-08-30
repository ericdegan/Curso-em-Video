la = float(input('Diga um numero: '))
lb = float(input('Diga um numero: '))
lc = float(input('Diga um numero: '))

a = (la + lb) > (lc)
b = (lb + lc) > (la)
c = (lc + la) > (lb)
tri = a,b,c
esc = (la != lb != lc)

if tri == (True, True, True):
    print('É possivel fazer um triangulo com essas medidas')
    if esc == (True):
        print('Sera um triangulo escaleno.')
    elif (la == lb != lc) or (la == lc != lb) or (lb == lc != la):
        print('Sera um triangulo isóceles.')
    elif la == lb == lc:
        print('Sera um triangulo equílatero.')
else:
    print('Você não pode fazer um triangulo.')
