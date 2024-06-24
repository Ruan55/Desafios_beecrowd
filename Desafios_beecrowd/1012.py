A, B, C = input().split()
A, B, C = float(A), float(B), float(C)

areaTrianguloRetangulo = (A * C) / 2
areaDoCirculo = 3.14159 * C**2
areaDoTrapezio = ((A + B) * C) / 2
areaDoQuadrado = B**2
areaDoRetangulo = A * B

print("TRIANGULO: {:.3f}".format(areaTrianguloRetangulo))
print("CIRCULO: {:.3f}".format(areaDoCirculo))
print("TRAPEZIO: {:.3f}".format(areaDoTrapezio))
print("QUADRADO: {:.3f}".format(areaDoQuadrado))
print("RETANGULO: {:.3f}".format(areaDoRetangulo))