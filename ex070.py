print('=-'*5, 'REGISTRANDO', '-='*5)

nome = str(input('Nome do produto:')).strip()
valor = float(input('Preço do produto R$: '))
barato = valor
caro = 0
total = valor
nomeb = ' '
if valor >= 1000:
    caro += 1
while True:
    cont = str(input('Deseja continuar? [s/n]: ')).upper()
    if cont == "S":
        nome = str(input('Nome do produto:')).strip()
        valor = float(input('Preço do produto R$: '))
        total += valor
        if valor < barato:
            barato = valor
            nomeb = nome
        if valor >= 1000:
            caro += 1
    if cont == 'N':
        break
    else:
        print('Não entendi sua resposta.')

print(f'Total gasto nesta compra foi de R$:{total:.2f}')
print(f'Existe {caro} produtos num valor maior de R$: 1000.00')
print(f'O nome do produto mais barato é {nomeb},com um valor de R$:{barato:.2f}')
