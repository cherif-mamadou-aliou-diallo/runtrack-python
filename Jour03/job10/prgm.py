def verifier_pair_impair(nombre):
    # Vérifier si le nombre est un entier positif
    if not isinstance(nombre, int) or nombre <= 0:
        return "Veuillez entrer un nombre entier et positif."

    # Vérifier si le nombre est pair ou impair
    if nombre % 2 == 0:
        return f"Le nombre {nombre} est pair."
    else:
        return f"Le nombre {nombre} est impair."

# Tester la fonction avec différentes valeurs
print(verifier_pair_impair(12))
print(verifier_pair_impair(9))
print(verifier_pair_impair(21))
print(verifier_pair_impair(28))

