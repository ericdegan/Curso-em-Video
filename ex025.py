c = str(input('Diga um nome: ')).strip()

cs = c.title()
cd = "Silva" in cs

print('Existe Silva no nome:{}? \n {}'.format(cs, cd))

#Poderia colocar o codigo tudo junto tbm, print('seu nome tem silva?{}'.format('silva' in nome.lower()))