c = str(input('Diga o nome da sua cidade: ')).strip()
cs = c.upper()
cd = cs.split()

#poderia ter usado o comando print(c[:5].upper() == "SANTO")


print('SANTO' in cd[0])