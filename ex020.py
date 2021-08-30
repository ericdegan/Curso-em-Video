import random
#a = "Juliana, Alfredo, Barbara, Jhonata"
#a1 = ('Juliana', 'Alfredo', 'Barbara', 'Jhonata')
#a2 = ('Alfredo', 'Barbara', 'Jhonata')
#a3 = ('Jhonata', 'Alfredo', 'Barbara', 'Juliana')
#a4 = ('Barbara', 'Jhonata', 'Juliana', 'Alfredo')
#print('Os alunos que irão apresentar seus trabalhos hoje seram', a)
#idx = random.randint(0, len(a1) -1)
#idc = random.randint(0, len(a2) -2)
#idi = random.randint(0, len(a3) -3)
#ido = random.randint(0, len(a4) -4)
#t = ('idx,idc,idi,ido')
#test = random.randint(0, len(t) -1)
#print(f'{t[test]}')
#print(f'E sera na seguinte sequencia 1º{a1[idx]}, 2º{a2[idc]}, 3º{a1[idi]}, 4º{a2[ido]}')
from random import shuffle
print('Hoje quatro alunos vão apresentar seus trabalho.')
a1 = input('Digam um nome: ')
a2 = input('Outro: ')
a3 = input('Outro: ')
a4 = input('Outro: ')

list = [a1, a2, a3, a4]

shuffle(list)


print('A sequencia sera esta:')
print(list)