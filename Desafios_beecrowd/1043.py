A, B, C = input().split()
A, B, C = float(A), float(B), float(C)

if A + B > C and A + C > B and B + C > A:
    perimetro = A + B + C
    print("Perimetro = {:.1f}".format(perimetro))
    
else:
    Areatrapezio = (A + B) * C / 2
    print("Area = {:.1f}".format(Areatrapezio))