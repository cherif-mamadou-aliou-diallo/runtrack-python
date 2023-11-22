# Initialisation des variables
montant_initial = 12000  # Montant initial de l'investissement en euros
taux_rendement_annuel = 7  # Taux de rendement annuel en pourcentage

# Affichage du gain annuel initial
gain_annuel = (taux_rendement_annuel / 100) * montant_initial
print("Gain annuel initial:", gain_annuel, "euros")

# L'investisseur augmente son capital de 5 000 euros et le taux augmente de 2%
montant_initial += 5000
taux_rendement_annuel += 2

# Calcul du nouveau gain annuel
nouveau_gain_annuel = (taux_rendement_annuel / 100) * montant_initial
print("Nouveau gain annuel après augmentation du capital et du taux:", nouveau_gain_annuel, "euros")

# L'investisseur retire 10% du montant total et le rendement diminue de 1%
retrait = 0.10 * montant_initial
montant_initial -= retrait
taux_rendement_annuel -= 1

# Calcul du montant final de l'investissement et du nouveau gain
montant_final = montant_initial * (1 + taux_rendement_annuel / 100)
nouveau_gain = montant_final - montant_initial
print("Montant final de l'investissement:", montant_final, "euros")
print("Nouveau gain après retrait et diminution du rendement:", nouveau_gain, "euros")
