def echange_premier_dernier(liste):
    if not liste:
        print("La liste est vide.")
        return

    # Échange des valeurs de la première et de la dernière case
    liste[0], liste[-1] = liste[-1], liste[0]

    # Affichage de la liste après l'échange
    print("Liste après l'échange :", liste)


ma_liste = [1, 2, 3, 4, 5]
echange_premier_dernier(ma_liste)
