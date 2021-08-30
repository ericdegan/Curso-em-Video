n1 = float(input('Quantos métros?'))

m = n1
c = n1*100
ml = n1*1000
km = n1/1000
em = n1/100
dm = n1/10

print('Hmm... {} metros?, quer dizer {:.0f} centimetros ou {:.0f} milimetros.'.format(m, c, ml))
print("Kilometros:{} Eqtometros:{} Decametros:{}".format(km, em, dm))