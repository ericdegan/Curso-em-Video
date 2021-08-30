import math

a = float(input('Diga o valor de um angulo:'))

sen = math.sin(math.radians(a))
cos = math.cos(math.radians(a))
tan = math.tan((math.radians(a)))

print("O seno de:{}º é {:.3f} o cosseno é {:.3f} e a tangente é {:.3f}".format(a, sen, cos, tan))