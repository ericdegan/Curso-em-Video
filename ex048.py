#print('Os numeros entre 1 e 500 que são multiplos de 3 são:')

#for c in range(0,500,3):
   #print(c)

########################################Exercicio certo#############################

print('Os numeros entre 1 e 500 que são multiplos de 3 são:')
soma = 0
cont = 0
for c in range(1,501,2):
   if c % 3  == 0:
       cont = cont + 1  #simplificado cont += 1
       soma = soma + c  #simplificado soma += c os dois teriam o mesmo resultado do usado.
print(soma)
print(cont)