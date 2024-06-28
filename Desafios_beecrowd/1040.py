n1, n2, n3, n4 = input().split()
n1, n2, n3, n4 = float(n1), float(n2), float(n3), float(n4)

peso1 = 2
peso2 = 3
peso3 = 4
peso4 = 1

media = (n1*peso1 + n2*peso2 + n3*peso3 + n4*peso4) / (peso1 + peso2 + peso3 + peso4)

if media >= 7.0:
    print("Media: {:.1f}".format(media))
    print("Aluno aprovado.")
elif media >= 5.0 and media <= 6.9:
    print("Media: {:.1f}".format(media))
    print("Aluno em exame.")
    notaExame = float(input())
    mediaExame = (notaExame + media) / 2 
    print("Nota do exame: {:.1f}".format(notaExame))
    print("Aluno aprovado.")
    print("Media final: {:.1f}".format(mediaExame))
else:
    print("Media: {:.1f}".format(media))
    print("Aluno reprovado.")