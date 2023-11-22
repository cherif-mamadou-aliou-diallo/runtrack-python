def est_premier(nombre):
    """Vérifie si un nombre est premier."""

    if nombre < 2:
        return False
    for i in range(2, int(nombre**0.5) + 1):
        if nombre % i == 0:
            return False
    return True

def afficher_nombres_premiers(maximum):
    """Affiche les nombres premiers jusqu'à un certain maximum."""
    for nombre in range(2, maximum + 1):
        if est_premier(nombre):
            print(nombre)

# Appel de la fonction pour afficher les nombres premiers jusqu'à 1000
afficher_nombres_premiers(1000)
