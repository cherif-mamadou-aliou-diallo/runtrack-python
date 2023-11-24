def liste_fruits():
    fruits = ["pomme", "cerise", "orange"]
    

    if len(fruits) >= 2:
        deuxieme_element = fruits[1]
        print("Le deuxième élément de la liste est :", deuxieme_element)
    else:
        print("La liste ne contient pas assez d'éléments.")


liste_fruits()
