def draw_rectangle(width, height):
    # Vérifier que la largeur et la hauteur sont positives
    if width <= 0 or height <= 0:
        print("Veuillez entrer des valeurs valides pour la largeur et la hauteur.")
        return

    # Première ligne du rectangle
    print('-' * width)

    # les lignes du milieu du rectangle
    for _ in range(height - 2):
        print('|' + ' ' * (width - 2) + '|')

    # Dernière ligne du rectangle
    if height > 1:
        print('-' * width)

# Exemple d'utilisation avec width=10 et height=3
draw_rectangle(10, 3)
