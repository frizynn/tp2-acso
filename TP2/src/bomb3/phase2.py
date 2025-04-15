def valid_phase2_pairs(xmin=-100000, xmax=100000):
    """
    returns a list of pairs (x, y) that satisfy:
      1) x + y == 49433
      2) x ≠ 0 and y ≠ 0  (i.e., x·y ≠ 0)
      3) the result of (x xor y), interpreted in 32 bits,
         is negative (its sign bit is 1)
    
    iterates over x in the range [xmin, xmax] and calculates y = 49433 - x.
    """
    resultados = []
    target_sum = 49433  # 0xc119 in decimal
    for X in range(xmin, xmax + 1):
        Y = target_sum - X
        # avoid either being 0 (since their product would be 0)
        if X == 0 or Y == 0:
            continue

        # simulate 32-bit xor: get the value in 32 bits
        xor_val = (X ^ Y) & 0xFFFFFFFF
        # in a 32-bit system, a number is negative if >= 0x80000000.
        if xor_val >= 0x80000000:
            resultados.append((X, Y))
    return resultados

def main():
    pares_validos = valid_phase2_pairs()
    print("pairs (x, y) that deactivate phase 2:")
    for X, Y in pares_validos:
        print(f"{X} {Y}")
    print(f"\ntotal valid combinations: {len(pares_validos)}")

if __name__ == "__main__":
    main()
