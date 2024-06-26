import math

A, B, C = input().split()
A, B, C = float(A), float(B), float(C)

delta = B ** 2 - 4 * A * C

if A == 0 or delta < 0:
    print("Impossivel calcular")
else:
    r1 = (- B + math.sqrt(delta)) / (2 * A)
    r2 = (- B - math.sqrt(delta)) / (2 * A)
    print("R1 = {:.5f}".format(r1))
    print("R2 = {:.5f}".format(r2))
