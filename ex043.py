altura = float(input('Qual sua altura: '))
peso = float(input('Qual seu peso: '))

imc = peso / (altura * 2)

print('Seu IMC é {:.1f}'.format(imc))
if imc <= 18.5:
    print('Você esta \033[37mABAIXO DO PESO.\033[m FRANGO DO CARALHO')
elif imc <= 25:
    print('Voce esta \033[32mNO PESO IDEAL.')
elif imc <= 30:
    print('Você esta \033[33mCOM SOBRE PESO.')
elif imc <= 40:
    print('Você esta \033[35mOBESO.')
else:
    print('Você sofre de \033[31mOBESIDADE MORBIDA.\033[m GORDO FILHO DA PUTA')
