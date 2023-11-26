def chiffre_cesar(message, decalage):
    message_chiffre = ""
    
    for char in message:
        if char.isalpha():  # Vérifie si le caractère est une lettre alphabétique
            # Détermine si le caractère est en majuscule ou en minuscule
            est_majuscule = char.isupper()
            
            # Applique le décalage à la lettre en utilisant la fonction ord() pour obtenir le code ASCII
            code_ascii = ord(char)
            nouveau_code_ascii = (code_ascii - ord('A' if est_majuscule else 'a') + decalage) % 26
            nouveau_char = chr(nouveau_code_ascii + ord('A' if est_majuscule else 'a'))
            
            # Ajoute le caractère chiffré au message final
            message_chiffre += nouveau_char
        else:
            # Si le caractère n'est pas une lettre alphabétique, le laisse inchangé
            message_chiffre += char
    
    return message_chiffre

# Exemple d'utilisation
message_original = "Hello, World!"
decalage = 3
message_chiffre = chiffre_cesar(message_original, decalage)
print("Message original:", message_original)
print("Message chiffré:", message_chiffre)
