n = int(input('Escrava um numero qualquer: '))

print('''Escolha para qual sistema você quer converter o seu numero:
    BINARIO [1]
    OCTAL [2]
    HEXDECIMAL [3]''')
esc = int(input('Qual você escolhe?  '))
if esc == 1:
    print('O numero {} em binario é:{}'.format(n, bin(n)[2:]))
elif esc == 2:
    print('O numero {} em octal é:{}'.format(n, oct(n)[2:]))           #AS DUAS PRIMEIRAS LETRAS DO NUMERO É SÓ A INDICAÇÃO DE QUAL SISTEMA É
else:                                                          #PARA SUMIR COM ISSO É SÓ USA O COMANDO [2:] QUE SERVE PARA MOSTRAR APENAS DA 3ª LETRA ADIANTE
    print('O numero {} em exadecimal é:{}'.format(n, hex(n)[2:]))



