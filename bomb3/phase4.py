from itertools import product

# Valores del array.0
array_values = [2, 13, 7, 14, 5, 10, 6, 15, 1, 12, 3, 4, 11, 8, 16, 9]

# Encontrar todas las combinaciones de 6 índices que sumen 59
def find_index_combinations(num_combinations=10):
    valid_combinations = []
    # Prueba todas las combinaciones posibles de 6 índices (0-15)
    for indices in product(range(16), repeat=6):
        sum_values = sum(array_values[idx] for idx in indices)
        if sum_values == 59:
            valid_combinations.append(indices)
            if len(valid_combinations) >= num_combinations:
                break
    return valid_combinations
# Encontrar caracteres ASCII imprimibles que al hacer AND con 0xF den el índice deseado
def find_matching_chars(index):
    matching_chars = []
    # Prueba caracteres ASCII imprimibles (32-126)
    for char_code in range(32, 127):
        if char_code & 0xF == index:
            matching_chars.append(chr(char_code))
    return matching_chars

# Generar una solución específica a partir de índices (como "1247JN")
def generate_specific_solution(indices):
    # Caracteres específicos para cada índice
    chars_map = {
        0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5',
        6: '6', 7: '7', 8: '8', 9: '9', 10: 'J', 11: 'K',
        12: 'L', 13: 'M', 14: 'N', 15: 'O'
    }
    return ''.join(chars_map[idx] for idx in indices)

# Encontrar todas las posibles soluciones
def find_all_solutions():
    valid_indices = find_index_combinations()
    solutions = []
    
    # Para cada combinación válida de índices
    for indices in valid_indices:
        # Encuentra caracteres que correspondan a cada índice
        chars_options = [find_matching_chars(idx) for idx in indices]
        
        # Si todos los índices tienen al menos un carácter correspondiente
        if all(chars_options):
            # Genera todas las combinaciones posibles de caracteres
            for chars in product(*chars_options):
                solutions.append(''.join(chars))
            
    return solutions

if __name__ == "__main__":
    # Ejecutar y mostrar resultados
    valid_indices = find_index_combinations()
    print(f"Encontradas {len(valid_indices)} combinaciones válidas de índices")

    # Mostrar algunas combinaciones de índices válidas (primeras 5)
    for i, indices in enumerate(valid_indices[:5]):
        values = [array_values[idx] for idx in indices]
        specific_solution = generate_specific_solution(indices)
        print(f"Combinación {i+1}: índices {indices} -> valores {values} -> suma {sum(values)}")
        print(f"Solución específica: '{specific_solution}'")
        
        # Explicación detallada de la solución
        print("Explicación:")
        for pos, idx in enumerate(indices):
            print(f"  Carácter {pos+1}: '{specific_solution[pos]}' -> AND 0xF = {idx} -> array[{idx}] = {array_values[idx]}")
        print()

    # También podemos mostrar algunas soluciones alternativas con diferentes caracteres
    print("\nAlgunas soluciones alternativas:")
    solutions = find_all_solutions()
    for i, solution in enumerate(solutions[:5]):
        if i < len(valid_indices):
            indices = valid_indices[i]
            print(f"Para índices {indices}: '{solution}'")