def custom_round(number):
    integer_part = int(number)
    decimal_part = number - integer_part

    if decimal_part >= 0.5:
        return integer_part + 1
    else:
        return integer_part

def custom_sort(arr):

    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

# Liste initiale
numbers = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

# Arrondir les nombres
rounded_numbers = [custom_round(num) for num in numbers]

# Trier les nombres arrondis
sorted_rounded_numbers = custom_sort(rounded_numbers)

# Afficher le résultat
print("Liste initiale:", numbers)
print("Liste arrondie et triée:", sorted_rounded_numbers)
