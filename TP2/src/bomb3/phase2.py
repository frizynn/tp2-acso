def valid_phase2_pairs(xmin=-100000, xmax=100000):
    """
    Retorna una lista de pares (X, Y) que cumplen con:
      1) X + Y == 49433
      2) X ≠ 0 y Y ≠ 0  (es decir, X·Y ≠ 0)
      3) El resultado de (X XOR Y), interpretado en 32 bits,
         es negativo (su bit de signo está en 1)
    
    Se itera sobre X en el rango [xmin, xmax] y se calcula Y = 49433 - X.
    """
    resultados = []
    target_sum = 49433  # 0xC119 en decimal
    for X in range(xmin, xmax + 1):
        Y = target_sum - X
        # Evitar que alguno sea 0 (pues su producto sería 0)
        if X == 0 or Y == 0:
            continue

        # Simular el XOR de 32 bits: obtener el valor en 32 bits
        xor_val = (X ^ Y) & 0xFFFFFFFF
        # En un sistema de 32 bits, un número es negativo si >= 0x80000000.
        if xor_val >= 0x80000000:
            resultados.append((X, Y))
    return resultados

def main():
    pares_validos = valid_phase2_pairs()
    print("Pares (X, Y) que desactivan la fase 2:")
    for X, Y in pares_validos:
        print(f"{X} {Y}")
    print(f"\nTotal de combinaciones válidas: {len(pares_validos)}")

if __name__ == "__main__":
    main()
