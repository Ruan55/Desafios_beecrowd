notas = int(input())

notas100 = notas // 100
notas50 = (notas % 100) // 50
notas20 = ((notas % 100) % 50) // 20
notas10 = (((notas % 100) % 50) % 20) // 10
notas5 = ((((notas % 100) % 50) % 20) % 10) // 5
notas2 = (((((notas % 100) % 50) % 20) % 10) % 5) // 2
notas1 = ((((((notas % 100) % 50) % 20) % 10) % 5) % 2) // 1
print(notas)
print("{} nota(s) de R$ 100,00".format(notas100))
print("{} nota(s) de R$ 50,00".format(notas50))
print("{} nota(s) de R$ 20,00".format(notas20))
print("{} nota(s) de R$ 10,00".format(notas10))
print("{} nota(s) de R$ 5,00".format(notas5))
print("{} nota(s) de R$ 2,00".format(notas2))
print("{} nota(s) de R$ 1,00".format(notas1))