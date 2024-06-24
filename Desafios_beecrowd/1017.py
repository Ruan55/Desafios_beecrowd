tempoGastoHoras = int(input())
velocidadeMediaKm = int(input())

quantidadeLitrosCombustivel = (tempoGastoHoras * velocidadeMediaKm) / 12

print("{:.3f}".format(quantidadeLitrosCombustivel))