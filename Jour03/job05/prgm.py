def calcule(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        
        if num2 != 0:
            return num1 / num2
        else:
            return "Division par zéro est indéfinie"
    elif operator == '%':
        
        if num2 != 0:
            return num1 % num2
        else:
            return "Modulo par zéro est indéfini"
    else:
        return "Opérateur non valide"

    
resultat_addition = calcule(8, '+', 13)
print("Addition:", resultat_addition)

resultat_soustraction = calcule(18, '-', 32)
print("Soustraction:", resultat_soustraction)

resultat_multiplication = calcule(14, '*', 26)
print("Multiplication:", resultat_multiplication)

resultat_division = calcule(14, '/', 42)
print("Division:", resultat_division)

resultat_modulo = calcule(25, '%', 9)
print("Modulo:", resultat_modulo)
