def time_to_text(minutes):
    # Calculer le nombre d'heures et de minutes
    hours = minutes // 60
    remaining_minutes = minutes % 60

    # chaîne de caractères
    if hours == 1:
        hours_string = "1 heure"
    else:
        hours_string = f"{hours} heures"

    if remaining_minutes == 1:
        minutes_string = "1 minute"
    else:
        minutes_string = f"{remaining_minutes} minutes"

    # le résultat
    print(f"{hours_string} et {minutes_string}")

# Exemple d'utilisation avec 160 minutes
time_to_text(160)
time_to_text(150)
time_to_text(230)
time_to_text(360)