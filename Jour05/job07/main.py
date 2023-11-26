def arrondir_notes(notes):
    notes_arrondies = []

    for note in notes:
        if note < 40:
            notes_arrondies.append(note)  # Les étudiants ayant moins de 40 échouent, pas d'arrondi
        else:
            prochain_multiple_de_5 = (note // 5 + 1) * 5
            difference = prochain_multiple_de_5 - note

            # Vérifie si la note doit être arrondie
            if difference < 3:
                notes_arrondies.append(prochain_multiple_de_5)
            else:
                notes_arrondies.append(note)

    return notes_arrondies

# Exemple
notes_originales = [34, 36, 42, 49, 58, 83, 79, 61, 91]
notes_arrondies = arrondir_notes(notes_originales)

# Affichage des résultats
print("Notes originales :", notes_originales)
print("Notes arrondies  :", notes_arrondies)
