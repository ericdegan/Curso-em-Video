import datetime

############################# OQUE ESTA EM COMENTARIO FUNCIONA TAMBEM ##################################
#dia = int(input('Que dia você nasceu: '))
#mes = int(input('Que mês: '))
#ano = int(input('Que ano: '))

#idade = datetime.date(ano, mes, dia)
#diferença = (datetime.date.today() - idade)  #
#dif = (diferença.days / 365.25)

ano = int(input('Que ano você nasceu: '))

atual = datetime.date.today().year
dif = atual - ano

print('O Atleta tem {} anos'.format(dif))


if dif <= 9:
  print('Você é da categoria MIRIM')
elif dif <= 14:
   print('Você é da categoria Infatil')
elif dif <= 19:
  print('Você é da categoria JUNIOR')
elif dif == 20:
   print('Você é da categoria SENIOR')
else:
   print('Você é da categoria MASTER')




