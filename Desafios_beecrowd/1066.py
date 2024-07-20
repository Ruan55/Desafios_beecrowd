numerosPares = 0
numerosImpares = 0 
numerosPositivos = 0
numerosNegativos = 0

for i in range(5):

    numeros = int(input())

    if numeros % 2 == 0:
        numerosPares += 1
    if numeros % 2 == 1:
        numerosImpares += 1
    if numeros > 0:
        numerosPositivos += 1
    if numeros < 0:
        numerosNegativos += 1

print(numerosPares, "valor(es) par(es)")
print(numerosImpares, "valor(es) impar(es)")
print(numerosPositivos, "valor(es) positivo(s)")
print(numerosNegativos, "valor(es) negativo(s)") 