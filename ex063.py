a = int(input('Quantos termos você deseja ver: '))
b = 0
c = 1
d = b + c
y = 3
print(b , end = '')
while y <= a +1:
    d = b+c
    print(' - {}'.format(d), end = '')
    b = c
    c = d
    y += 1

"""SEQUENCIA DE FIBONACCI"""
