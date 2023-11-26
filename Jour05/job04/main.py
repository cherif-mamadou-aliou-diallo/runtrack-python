def draw_diagonal_carpet(n):
    # Vérifier que la taille est positive
    if n <= 0:
        print("Veuillez entrer une taille positive.")
        return

    # Dessiner le tapis
    for i in range(n + 1):
        for j in range(n + 1):
            # la diagonale
            if i == j:
                print('/', end='')
            # les autres caractères du tapis
            else:
                print('*', end='')

        # Aller à la ligne pour la prochaine rangée
        print()

# Exemple d'utilisation avec une taille de 10
draw_diagonal_carpet(10)
