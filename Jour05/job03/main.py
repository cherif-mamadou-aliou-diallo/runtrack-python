def draw_triangle(height):
    # Vérifier que la hauteur est positive
    if height <= 0:
        print("Veuillez entrer une valeur positive pour la hauteur.")
        return

    # Dessiner le triangle
    for i in range(1, height + 1):
        # les espaces avant le premier caractère
        print(' ' * (height - i), end='')

        # le caractère '/'
        print('/', end='')

        # les caractères '_' au milieu
        if i > 1 and i < height:
            print('_' * (2 * (i - 1) - 1), end='')

        # le caractère '\' sauf pour la première ligne
        if i > 1:
            print('\\', end='')

        # Aller à la ligne pour la prochaine rangée
        print()

# Exemple d'utilisation avec height=5
draw_triangle(5)
