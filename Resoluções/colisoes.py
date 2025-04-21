def verificar(ret1, ret2):
    x0A, y0A, x1A, y1A = ret1
    x0B, y0B, x1B, y1B = ret2

    if x1A <= x0B or x1B <= x0A or y1A <= y0A or y1A <= y0A:
        print(0)
    else:
        print(1)


print("Digite as coordenadas do primeiro retangulo:")
x0A = int(input("x0: "))
y0A = int(input("y0: "))
x1A = int(input("x1: "))
y1A = int(input("y1: "))
ret1 = [x0A, y0A, x1A, y1A]

print("Digite as coordenadas do segundo retangulo:")
x0B = int(input("x0: "))
y0B = int(input("y0: "))
x1B = int(input("x1: "))
y1B = int(input("y1: "))
ret2 = [x0B, y0B, x1B, y1B]

verificar(ret1, ret2)
