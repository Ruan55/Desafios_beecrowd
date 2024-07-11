vertebradoOuInvertebrado = str(input())

if vertebradoOuInvertebrado == "vertebrado":
    # Aves
    aveOuMamifero = str(input())
    if aveOuMamifero == "ave":
        carnivoroOuOnivoro = str(input())
        if carnivoroOuOnivoro == "carnivoro":
            print("aguia")
        elif carnivoroOuOnivoro == "onivoro":
            print("pomba")
    # Mamiferos
    elif aveOuMamifero == "mamifero":
        onivoroOuHerbivoro = str(input())
        if onivoroOuHerbivoro == "onivoro":
            print("homem")
        elif onivoroOuHerbivoro == "herbivoro":
            print("vaca")

if vertebradoOuInvertebrado == "invertebrado":
    # Inseto
    insetoOuAnelideo = str(input())
    if insetoOuAnelideo == "inseto":
        hematofagoOuHerbivoro = str(input())
        if hematofagoOuHerbivoro == "hematofago":
            print("pulga")
        elif hematofagoOuHerbivoro == "herbivoro":
            print("lagarta")
    # Anelideo
    elif insetoOuAnelideo == "anelideo":
        hematofagoOuOnivoro = str(input())
        if hematofagoOuOnivoro == "hematofago":
            print("sanguessuga")
        elif hematofagoOuOnivoro == "onivoro":
            print("minhoca")