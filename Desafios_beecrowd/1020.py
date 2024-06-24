idadeEmDias = int(input())

ano = idadeEmDias // 365
mes = (idadeEmDias % 365) // 30
dia = (idadeEmDias % 365) % 30

print("{} ano(s)".format(ano))
print("{} mes(es)".format(mes))
print("{} dia(s)".format(dia))