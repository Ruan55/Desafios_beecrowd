numero = 0
soma = 0

for i in range(6):

    numeros = float(input())

    if numeros > 0:
        numero += 1
        soma += numeros
    else:
        numero == 0

media = soma / numero

print(numero, "valores positivos")
print("{:.1f}".format(media))