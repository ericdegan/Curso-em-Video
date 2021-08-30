salario = float(input('Qual o seu salario R$: '))

print('Você tem um aumento de 10% no seu salario'if salario >= 1250.0 else 'Você tera um aumento de 15% no seu salario')

if salario >= 1250.0:
    a1 = (salario/100 * 10) + salario
    print('Agora seu salario sera R$:{:.2f}'.format(a1))
else:
    a2 = (salario/100 * 15) + salario
    print('Agora seu salario vai ser R$:{:.2f}'.format(a2))