from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
ano = (18 - idade) + atual
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
if idade == 18:
    print('Você tem que se alistar esse ano!')
elif idade <= 14:
    print('Saía daqui seu merdinha!')
elif idade <= 17:
    print('Você tera que se alistar em breve garoto, em {}'.format(ano))
elif idade >= 30:
    print('Você já passou e muito da idade de se alistar seu lixo! Era para ter se alistado em {}'.format(ano))
else:
    print('Você já passou da idade de se alistar.')




############################## AQUI EM BAIXO FOI A FORMA QUE EU FIZ SOZINHO ##################################






#from time import sleep
#print('Quero saber quando posso me alistar.')
#sleep(.8)
#ano = int(input('Me diga em que ano voce nasceu: '))
#mes = int(input('Em que mês: '))
#dia = int(input('Que dia: '))


#if dia > 31 or mes > 12 or ano > 2021:
#    print('Esta data não existe')
#elif ano < 2003:
#    bl = (ano - 2003) + 2021
#    print('Você ja passou do ano do seu alistamento, você deveria ter se alistado em {}'.format(bl))
#elif ano > 2003:
#    al = ano - 2003
#    a = al + 2021
#    print('Você podera se alistar daqui {} anos, ou seja em {}'.format(al, a))
#else:
#    print('Você precisa se alistar este ano!')