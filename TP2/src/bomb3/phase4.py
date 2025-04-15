from itertools import product

# array values
array_values = [2, 13, 7, 14, 5, 10, 6, 15, 1, 12, 3, 4, 11, 8, 16, 9]

# find all combinations of 6 indices that sum to 59
def find_index_combinations(num_combinations=10):
    valid_combinations = []
    # try all possible combinations of 6 indices (0-15)
    for indices in product(range(16), repeat=6):
        sum_values = sum(array_values[idx] for idx in indices)
        if sum_values == 59:
            valid_combinations.append(indices)
            if len(valid_combinations) >= num_combinations:
                break
    return valid_combinations
# find printable ascii characters that when and'ed with 0xf give the desired index
def find_matching_chars(index):
    matching_chars = []
    # try printable ascii characters (32-126)
    for char_code in range(32, 127):
        if char_code & 0xF == index:
            matching_chars.append(chr(char_code))
    return matching_chars

# generate a specific solution from indices (like "1247JN")
def generate_specific_solution(indices):
    # specific characters for each index
    chars_map = {
        0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5',
        6: '6', 7: '7', 8: '8', 9: '9', 10: 'J', 11: 'K',
        12: 'L', 13: 'M', 14: 'N', 15: 'O'
    }
    return ''.join(chars_map[idx] for idx in indices)

# find all possible solutions
def find_all_solutions():
    valid_indices = find_index_combinations()
    solutions = []
    
    # for each valid combination of indices
    for indices in valid_indices:
        # find characters that correspond to each index
        chars_options = [find_matching_chars(idx) for idx in indices]
        
        # if all indices have at least one corresponding character
        if all(chars_options):
            # generate all possible combinations of characters
            for chars in product(*chars_options):
                solutions.append(''.join(chars))
            
    return solutions

if __name__ == "__main__":
    # run and show results
    valid_indices = find_index_combinations()
    print(f"found {len(valid_indices)} valid index combinations")

    # show some valid index combinations (first 5)
    for i, indices in enumerate(valid_indices[:5]):
        values = [array_values[idx] for idx in indices]
        specific_solution = generate_specific_solution(indices)
        print(f"combination {i+1}: indices {indices} -> values {values} -> sum {sum(values)}")
        print(f"specific solution: '{specific_solution}'")
        
        # detailed explanation of the solution
        print("explanation:")
        for pos, idx in enumerate(indices):
            print(f"  character {pos+1}: '{specific_solution[pos]}' -> and 0xf = {idx} -> array[{idx}] = {array_values[idx]}")
        print()

    # we can also show some alternative solutions with different characters
    print("\nsome alternative solutions:")
    solutions = find_all_solutions()
    for i, solution in enumerate(solutions[:5]):
        if i < len(valid_indices):
            indices = valid_indices[i]
            print(f"for indices {indices}: '{solution}'")