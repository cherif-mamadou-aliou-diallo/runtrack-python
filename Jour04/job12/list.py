def tri_bulles(liste):
    n = len(liste)
    
    for i in range(n):
        # Derniers i éléments déjà triés, pas besoin de les re-vérifier
        for j in range(0, n-i-1):
            # Échanger les éléments s'ils sont dans le mauvais ordre
            if liste[j] > liste[j+1]:
                liste[j], liste[j+1] = liste[j+1], liste[j]

ma_liste = [64, 34, 25, 12, 22, 11, 90]
tri_bulles(ma_liste)

print("Liste triée :", ma_liste)
