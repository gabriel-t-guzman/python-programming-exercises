def find_combinations(target, numbers):
    # Inicializar DP
    dp = {i: [] for i in range(target + 1)}
    dp[0] = [[]]  # Solo hay una forma de formar 0: con nada

    # Iterar sobre cada número en el conjunto
    for num in numbers:
        for i in range(num, target + 1):  # Comenzar desde num para no exceder límites
            for combination in dp[i - num]:
                dp[i].append(combination + [num])
    print (dp)            
    return dp[target]

# Ejemplo
target = 12
numbers = [10, 5, 2, 1]


combinations = find_combinations(target, numbers)
