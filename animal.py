tipo_animal = str(input())

if tipo_animal == "vertebrado":
    tipo_vertebrado = str(input())
    if tipo_vertebrado == "ave":
        tipo_ave = str(input())
        if tipo_ave == "carnivoro":
            print("aguia")
        elif tipo_ave == "onivoro":
            print("pomba")
    elif tipo_vertebrado == "mamifero":
        tipo_mamifero = str(input())
        if tipo_mamifero == "onivoro":
            print("homem")
        elif tipo_mamifero == "herbivoro":
            print("vaca")

if tipo_animal == "invertebrado":
    tipo_invertebrado = str(input())
    if tipo_invertebrado == "inseto":
        tipo_inseto = str(input())
        if tipo_inseto == "hematofago":
            print("pulga")
        elif tipo_inseto == "herbivoro":
            print("lagarta")
    elif tipo_invertebrado == "anelideo":
        tipo_analideo = str(input())
        if tipo_analideo == "hematofago":
            print("sanguessuga")
        elif tipo_analideo == "onivoro":
            print("minhoca")