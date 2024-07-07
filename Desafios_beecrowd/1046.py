horaInicial, horaFinal = input().split()
horaInicial, horaFinal = int(horaInicial), int(horaFinal)
    
if horaInicial > horaFinal:
    duracaoJogo = (24 + horaFinal) - horaInicial
    print("O JOGO DUROU {} HORA(S)".format(duracaoJogo))
elif horaInicial < horaFinal:
    duracaoJogo = horaFinal - horaInicial
    print("O JOGO DUROU {} HORA(S)".format(duracaoJogo))
else:
    duracaoJogo = 24 - 0
    print("O JOGO DUROU {} HORA(S)".format(duracaoJogo))