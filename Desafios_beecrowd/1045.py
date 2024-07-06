A, B, C = input().split()
A, B, C = float(A), float(B), float(C)

if A < B:
    maior = A
    A = B
    B = maior

if A < C:
    maior = A
    A = C
    C = maior

if B < C:
    maior = B
    B = C
    C = maior
    
if A >= B + C:
    print("NAO FORMA TRIANGULO")
else:   
    if A*A == B*B + C*C:
        print("TRIANGULO RETANGULO")
    if A*A > B*B + C*C:
        print("TRIANGULO OBTUSANGULO")
    if A*A < B*B + C*C:
        print("TRIANGULO ACUTANGULO")
        
    if A == B and A == C and B == C:
        print("TRIANGULO EQUILATERO")
    else:
        if A == B or A == C or B == C:
            print("TRIANGULO ISOCELES")

