def distance_totale_semaine(marches, hauteur_marche):
    nombre_jours_semaine = 7
    nombre_allers_retours_par_jour = 2
    hauteur_marche_m = hauteur_marche / 100  # Conversion de cm en m

    distance_par_aller_retour = marches * hauteur_marche_m
    distance_totale = distance_par_aller_retour * nombre_allers_retours_par_jour * nombre_jours_semaine

    return distance_totale

# Exemple 
nombre_marches = 10
hauteur_marche_cm = 20
resultat_distance = distance_totale_semaine(nombre_marches, hauteur_marche_cm)

# résultat
print(f"Pour {nombre_marches} marches de {hauteur_marche_cm} cm, le gardien parcourt {resultat_distance:.2f} m par semaine.")
