codigo, quantidade = input().split()
codigo, quantidade = int(codigo), int(quantidade)

if codigo == 1:
    resultado = 4.00 * quantidade
    print("Total: R$ {:.2f}".format(resultado))
elif codigo == 2:
    resultado = 4.50 * quantidade
    print("Total: R$ {:.2f}".format(resultado))
elif codigo == 3:
    resultado = 5.00 * quantidade
    print("Total: R$ {:.2f}".format(resultado))
elif codigo == 4:
    resultado = 2.00 * quantidade
    print("Total: R$ {:.2f}".format(resultado))
elif codigo == 5:
    resultado = 1.50 * quantidade
    print("Total: R$ {:.2f}".format(resultado))