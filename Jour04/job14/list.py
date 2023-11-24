def my_long_word(n, phrase):
    mots = []
    mot_actuel = ""
    
    for char in phrase:
        if char.isalnum() or char == "'":
            mot_actuel += char
        elif mot_actuel:
            if len(mot_actuel) > n:
                mots.append(mot_actuel)
            mot_actuel = ""
    
    if mot_actuel and len(mot_actuel) > n:
        mots.append(mot_actuel)
    
    return " ".join(mots)

# Exemple
resultat = my_long_word(3, "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance")
print("Output:", resultat)
