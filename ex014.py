temp = float(input('Diga uma temperatura em ºC:'))

f1 = temp * 1.8 + 32
k1 = temp + 273.16

tc = input('{}ºC é = \n {}ºF \n {} Kelvin'.format(temp,f1,k1))

tempf = float(input('Diga uma temperatura em ºF:'))

fc1 = (tempf - 32) / 9
fc2 = fc1 * 5
fk = fc2 + 273.16

TF = input('{}ºF = {:.1f}ºC e {}K'.format(tempf, fc2, fk))

tempk = float(input('Diga uma temperatura em K:'))

kc = tempk - 273
kf = kc * 1.8 + 32

TK = print('{}K = {:.1f}ºF e {:.1f}ºC'.format(tempk, kf, kc))


