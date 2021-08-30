a = int(input("Diga um numero: "))
b = int(input('Diga outro numero: '))
c = int(input('Diga mais um numero: '))

n1 = bool(a > b) , (a > c)
n2 = bool(b > c) , (b > a)
n3 = (c > a) , (c > b)

print(n1)
print(n2)
print(n3)

if n1 == (False, False):
    print(a, 'é o menor numero')
if n2 == (False, False):
    print(b, 'é o menor numero')
if n3 == (False, False):
    print(c, 'é o menor numero')
# -------------------------------------------------------------------------------------------- #
if n1 == (True, True):
    print(a, 'é o maior numero')
if n2 == (True, True):
    print(b, 'é o maior numero')
if n3 == (True, True):
    print(c, 'é o maior numero')