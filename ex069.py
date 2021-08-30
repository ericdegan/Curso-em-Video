print('->'*5,'Cadastro', '<-'*5)
fm = 0
qnt = 0
mm = 0
maior = 0
idade = int(input('Qual a idade desta pessoa: '))
sexo = str(input('Qual sexo dessa pessoa [M/F]: ')).upper()
if idade >= 18:
    maior += 1
if idade <= 20:
    fm += 1
while True:
    cont = str(input('Deseja continuar? [s/n]: ')).upper()
    if cont == "S":
        idade = int(input('Qual a idade desta pessoa: '))
        sexo = str(input('Qual sexo dessa pessoa [M/F]: ')).upper()
        if sexo == "F":
            qnt += 1
            if idade <= 20:
                fm += 1
            if idade >= 18:
                maior += 1
        elif sexo == "M":
            mm += 1
            qnt += 1
            if idade >= 18:
                maior += 1
        else:
            sexo = str(input('Qual sexo dessa pessoa [M/F]: ')).upper()
    else:
        break
if mm != 1:
    print(f'No cadastro existem {mm} são homens.')
else:
    print(f'No cadastro existe {mm} homem.')
if fm !=1:
    print(f'{fm} são mulheres menores de 20 anos.')
else:
    print(f'{fm} é mulher menor de 20 anos.')
if maior != 1:
    print(f'{maior} pessoas maiores de Idade,')
else:
    print(f'{maior} pessoa maior de Idade,')
