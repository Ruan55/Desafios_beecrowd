numerosPar = 0

for i in range(5):

    numeros = int(input())

    if numeros % 2 == 0:
        numerosPar += 1
    else:
        numerosPar == 0

print(numerosPar, "valores pares")