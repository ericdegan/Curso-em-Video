soma = 0
qnt = 0

while True:
    n = int(input('Digite um numero para ser somado: '))
    soma += n
    qnt += 1
    if n != 999:
        prox = str(input('Quer Continuar [S/N]:')).upper()
        if prox == 'S':
            print('OK')
        else:
            break
print(f'Você digitou [{qnt}] numeros e a soma dos numeros que você digitou é [{soma - 999}]')