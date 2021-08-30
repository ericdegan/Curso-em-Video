la = float(input('Diga um numero: '))
lb = float(input('Diga um numero: '))
lc = float(input('Diga um numero: '))

a = (la - lb) < (lc) < (la - lb)
b = (lb - lc) < (la) < (lb + lc)
c = (lc - la) < (lb) < (lc - la)

tri = a,b,c

if tri == (False, False, False):
    print('Não é possivel fazer um triangulo com essas medidas')
else:
    print('Você pode fazer um triangulo com essa medida.')




