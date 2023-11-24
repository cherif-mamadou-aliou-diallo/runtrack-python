L = [1, 2, 3, 4, 5]

print("Deuxième valeur de la liste :", L[1])

# fonction qui remplace L[3] par la somme des cases voisines L[2] & L[4]
def remplacer_valeur(index):
    L[index] = L[index-1] + L[index+1]

# la fonction pour remplacer L[3]
remplacer_valeur(3)

# Afficher à nouveau le tableau
print("Tableau après remplacement de L[3] :", L)

# Afficher la dernière valeur de la liste
print("Dernière valeur de la liste :", L[-1])
