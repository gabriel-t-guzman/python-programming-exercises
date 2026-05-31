def find_combinations_backtracking(target, numbers):
    def backtrack(remaining, start, current_combination, result):
        if remaining == 0:  # Si alcanzamos la meta, guardamos la combinación
            result.append(list(current_combination))
            return
        if remaining < 0:  # Si pasamos la meta, retrocedemos
            return

        for i in range(start, len(numbers)):
            current_combination.append(numbers[i])
            backtrack(remaining - numbers[i], i, current_combination, result)  # Permitir reutilizar números
            current_combination.pop()  # Eliminar el número agregado para explorar otras posibilidades

    result = []
    backtrack(target, 0, [], result)
    return result

numbers = [10, 5, 2, 1]
target = 12
combinations = find_combinations_backtracking(target, numbers)
print(combinations)

