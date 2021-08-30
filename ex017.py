from math import hypot

co = float(input("Cateto oposto: "))
ca = float(input('Cateto adjacent: '))

hip = hypot(co, ca)

print('A hipotenusa deste triangulo é:{:.2f}'.format(hip))