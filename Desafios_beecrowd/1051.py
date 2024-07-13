salarioPessoa = float(input())

impostoDeRenda = 0
if salarioPessoa >= 0 and salarioPessoa <= 2000:
    print("Isento")
elif salarioPessoa >= 2000.01 and salarioPessoa <= 3000:
    impostoDeRenda = (salarioPessoa - 2000) * 0.08
    print("R$ {:.2f}".format(impostoDeRenda))
elif salarioPessoa >= 3000.01 and salarioPessoa <= 4500:
    impostoDeRenda = 1000 * 0.08 + (salarioPessoa - 3000) * 0.18
    print("R$ {:.2f}".format(impostoDeRenda))
elif salarioPessoa > 4500:
    impostoDeRenda = 1000 * 0.08 + 1500 * 0.18 + (salarioPessoa - 4500) * 0.28
    print("R$ {:.2f}".format(impostoDeRenda))

