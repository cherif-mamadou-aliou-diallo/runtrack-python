def compter_multiples_de_trois(liste):
    # Initialiser le compteur
    count = 0

    # Parcourir chaque élément de la liste
    for nombre in liste:
        # Vérifier si l'élément est un multiple de 3
        if nombre % 3 == 0:
            count += 1

    # le résultat
    print("Nombre de multiples de 3 dans la liste :", count)

ma_liste = [8, 24, 48, 2, 16]
compter_multiples_de_trois(ma_liste)

