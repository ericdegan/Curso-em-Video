#import random
#print('Hoje quero sortear 1 dos 4 dos melhores alunos da sua classe')
#nomes = ('Juarez', 'Ronaldo', 'Ricardo', 'Eduardo')
#print('Os participantes são', nomes)
#name = ('Juarez', 'silvano')
#idx = random.randint(0, len(nomes) -1)
#print(f'O sorteado foi: {nomes[idx]}')
import random

n1 = input('Escreva um nome: ')
n2 = input('Escreva um nome: ')
n3 = input('Escreva um nome: ')
n4 = input('Escreva um nome: ')
list = [n1, n2, n3, n4]

escolhido = random.choice(list)

print('O Aluno escolhido foi:{}'.format(escolhido))