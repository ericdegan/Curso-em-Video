n = input('Escrava algo ')
print('É AlfaNumérico:' ,n.isalnum()) #Quando é uma letra é um numero juntos
print('É uma letra:', n.isalpha())
print( 'É um ascii:' , n.isascii())
print('É um dígito:', n.isdigit())
print('É Minusculo:', n.islower())
print('É Maiusculo:', n.isupper())
print('É decimal:', n.isdecimal())
print('É um indentificador:', n.isidentifier())
print('É um numero:', n.isnumeric())
print('É capaz de correr:', n.isprintable())
print('É um espaço:', n.isspace())
print('É Capitalizado:',n.istitle()) #Capitalizado é quando começa com letras maiusculas ex: São Bernado Do Campo.