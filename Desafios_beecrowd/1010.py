codigo1, quantidade1, valor1 = input().split()
codigo1, quantidade1, valor1 = int(codigo1), int(quantidade1), float(valor1)

codigo2, quantidade2, valor2 = input().split()
codigo2, quantidade2, valor2 = int(codigo2), int(quantidade2), float(valor2)

totalGeral = (quantidade1 * valor1) + (quantidade2 * valor2)

print("VALOR A PAGAR: R$ {:.2f}".format(totalGeral))