nome = input('Diga seu nome completo:').strip()

print('{}'.format(nome.upper()))
print('{}'.format(nome.lower()))



nomed = nome.split() #Para isso poderia ter usado o comando nome.find(' ') no format
nomedc = nomed[0]
print('O primeiro nome tem {} letras'.format(len(nomedc)))

fl = nome.split() #Poderia ter feito isso também colocando assim no .format(len(nome) - nome.count(' ')
ls = ''.join(fl)

print(ls)

print('Seu nome tem {} letras ao todo'.format(len(ls)))



