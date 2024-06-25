valor = int(input())

notas = [100, 50, 20, 10, 5, 2, 1]

for nota in notas:
    quantidadeNotas = int(valor / nota)
    print("{} nota(s) de R$ {:.2f}".format(quantidadeNotas, nota))
    valor -= quantidadeNotas * nota
