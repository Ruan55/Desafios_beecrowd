salarioFuncionario = float(input())

if salarioFuncionario >= 0 and salarioFuncionario <= 400:
    aumento = salarioFuncionario * 0.15
    newSalario = aumento + salarioFuncionario
    print("Novo salario: {:.2f}".format(newSalario))
    print("Reajuste ganho: {:.2f}".format(aumento))
    print("Em percentual: 15 %")
elif salarioFuncionario >= 400.01 and salarioFuncionario <= 800:
    aumento = salarioFuncionario * 0.12
    newSalario = aumento + salarioFuncionario
    print("Novo salario: {:.2f}".format(newSalario))
    print("Reajuste ganho: {:.2f}".format(aumento))
    print("Em percentual: 12 %")
elif salarioFuncionario >= 800.01 and salarioFuncionario <= 1200:
    aumento = salarioFuncionario * 0.10
    newSalario = aumento + salarioFuncionario
    print("Novo salario: {:.2f}".format(newSalario))
    print("Reajuste ganho: {:.2f}".format(aumento))
    print("Em percentual: 10 %")
elif salarioFuncionario >= 1200.01 and salarioFuncionario <= 2000:
    aumento = salarioFuncionario * 0.07
    newSalario = aumento + salarioFuncionario
    print("Novo salario: {:.2f}".format(newSalario))
    print("Reajuste ganho: {:.2f}".format(aumento))
    print("Em percentual: 7 %")
else:
    aumento = salarioFuncionario * 0.04
    newSalario = aumento + salarioFuncionario
    print("Novo salario: {:.2f}".format(newSalario))
    print("Reajuste ganho: {:.2f}".format(aumento))
    print("Em percentual: 4 %")