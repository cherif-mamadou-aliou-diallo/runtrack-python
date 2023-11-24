def supprimer_doublons(liste):
    liste_sans_doublons = []

    for element in liste:
        # Ajoute l'élément à la nouvelle liste s'il n'est pas déjà présent
        if element not in liste_sans_doublons:
            liste_sans_doublons.append(element)

    return liste_sans_doublons

ma_liste = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
nouvelle_liste = supprimer_doublons(ma_liste)

print("Liste initiale :", ma_liste)
print("Liste sans doublons :", nouvelle_liste)
