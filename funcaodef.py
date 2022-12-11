def perimetro(b, h):
    p = 2 * b + 2 *h
    return p

def area(b, h):
    a = b * h
    return a

base = float(input('informe a base: '))
alt = float(input('infome a altura: '))
per = perimetro(base, alt)
ar = area(base, alt)

print('perimetro: ', per)
print('aea: ', ar)