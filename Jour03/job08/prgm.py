def produits(type, saison):
    if type == "fruits":
        if saison == "hiver":
            print("orange, mandarine et kiwi")
        elif saison == "ete":
            print("Poire, fraise, cassis")
        else:
            print("Saison invalide pour le type de produit 'fruits'")
    elif type == "legume":
        if saison == "hiver":
            print("carotte, topinambour, endive")
        elif saison == "ete":
            print("artichaut, aubergine, navet")
        else:
            print("Saison invalide pour le type de produit 'legume'")
    else:
        print("Type de produit invalide")


produits("fruits", "hiver")
produits("fruits", "ete")
produits("legume", "hiver")
produits("legume", "ete")
