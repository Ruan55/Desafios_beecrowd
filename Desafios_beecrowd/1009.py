nomeVendedor = str(input())
salarioFixo = float(input())
totalDeVendas = float(input())

salarioFinal = salarioFixo + totalDeVendas * 0.15

print("TOTAL = R$ {:.2f}".format(salarioFinal))