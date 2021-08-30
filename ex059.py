c = 1
mn = 0
while c != 0:
    n1 = int(input('Digite um numero: '))
    n2 = int(input('Digite um numero: '))
    r = int(input('''Oque deseja fazer com esses numero?
     [1]Somar
     [2]Mutiplicar
     [3]Maior
     [4]Novos números
     [5]Sair do programa
      '''))
    if r == 1:
        print('A soma de {} + {} é: {}'.format(n1, n2, n1 + n2))
    elif r == 2:
        print('A multiplicação dos numeros {} e {} é igual: {}'.format(n1, n2,n1*n2))
    elif r == 3:
        if n1>n2:
            mn = n1
        else:
            mn = n2
        print('O maior numero digitado é {}'.format(mn))
    elif r == 4:
        print('Ok')
    elif r == 5:
        c = 0
    else:
        print('Opção invalida. Tente novamente')
print('Programa encerrado!')





