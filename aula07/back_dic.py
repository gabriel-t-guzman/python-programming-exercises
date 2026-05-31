#pra todas
def find_all_combinations(n, values, index=0, current_combination=None, results=None):
    if current_combination is None:
        current_combination = {}
    if results is None:
        results = []
    
    # Caso base: si alcanzamos exactamente el objetivo
    if n == 0:
        results.append(current_combination.copy())
        return
    
    # Caso recursivo: recorrer los valores restantes
    for i in range(index, len(values)):
        value = values[i]
        if value <= n:  # Solo considerar valores que caben
            # Añadir este valor a la combinación actual
            count = n // value
            current_combination[value] = count
            # Restar el valor y continuar con el siguiente índice
            find_all_combinations(n % value, values, i + 1, current_combination, results)
            # Eliminar el valor agregado al retroceder
            del current_combination[value]
    
    return results

# Ejemplo de uso
n = 12
values = [10, 5, 2, 1]
all_combinations = find_all_combinations(n, values)
for combination in all_combinations:
    print(combination)

#para 1 

def find_linear_combination(n, values):
    combination = {}
    for value in values:
        # Dividir para saber cuántas veces se usa el valor
        count = n // value
        if count > 0:
            combination[value] = count
        # Calcular el residuo restante
        n = n % value

    return combination

# Ejemplo de uso
n = 157
values = [10, 5, 2, 1]
result = find_linear_combination(n, values)
print(result)

