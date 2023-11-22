chaine = "abcdefghijklmnopqrstuvwxyz"[:10]

for i in range(1, len(chaine) + 1):
    espace = " " * (len(chaine) - i)
    partie_gauche = chaine[:i]
    partie_droite = chaine[:i-1][::-1]
    ligne = espace + partie_gauche + partie_droite
    print(ligne)
