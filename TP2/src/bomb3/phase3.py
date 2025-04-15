def strcompare(a: str, b: str) -> int:
    """
    Compara dos cadenas de forma lexicográfica.
      Retorna 0 si son iguales,
      Retorna un valor negativo si 'a' es menor que 'b',
      Retorna un valor positivo si 'a' es mayor que 'b'.
    """
    if a == b:
        return 0
    elif a < b:
        return -1
    else:
        return 1

def explode_bomb():
    """Simula la explosión de la bomba lanzando una excepción."""
    raise Exception("¡La bomba ha explotado! Error en los parámetros de búsqueda.")

def cuenta(input_str: str, palabras: list, low: int, high: int) -> int:
    """
    Función recursiva que implementa una búsqueda binaria similar al código ensamblador.
    
    Parámetros:
      - input_str: palabra de entrada que se desea buscar.
      - palabras: lista de palabras (se asume ordenada).
      - low: índice inferior del rango.
      - high: índice superior del rango.
    
    La función calcula el índice medio usando la fórmula:
          mid = (low & high) + ((low ^ high) >> 1)
    y luego compara `input_str` con la palabra en dicha posición. Si la comparación da 0,
    retorna el valor ASCII del primer carácter de la palabra encontrada; si no, realiza
    llamadas recursivas acumulando ese valor.
    
    Si en algún momento el rango no es válido (por ejemplo, high <= mid o low >= mid),
    se simula la explosión de la bomba.
    """
    if low > high:
        explode_bomb()

    mid = (low & high) + ((low ^ high) >> 1)
    if mid < 0 or mid >= len(palabras):
        explode_bomb()

    current_word = palabras[mid]
    cmp_result = strcompare(input_str, current_word)
    first_char_val = ord(current_word[0])
    
    if cmp_result == 0:
        return first_char_val
    elif cmp_result > 0:
        if high <= mid:
            explode_bomb()
        return first_char_val + cuenta(input_str, palabras, mid + 1, high)
    else:
        if low >= mid:
            explode_bomb()
        return first_char_val + cuenta(input_str, palabras, low, mid - 1)

def main():
    import sys

    # Lee el archivo "bomb3/palabras.txt"
    try:
        with open("bomb3/palabras.txt", "r", encoding="utf-8") as file:
            # Se remueven líneas vacías y se elimina espacios en blanco
            palabras = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print("Error: No se encontró el archivo 'bomb3/palabras.txt'.")
        sys.exit(1)

    if not palabras:
        print("Error: La lista de palabras está vacía.")
        sys.exit(1)

    # Ordena la lista (la búsqueda binaria asume que está ordenada)
    palabras.sort()

    print("Buscando palabras que cumplan con la condición de la Fase 3:")
    print("El resultado (valor de 'cuenta') debe estar entre 401 y 799.\n")

    valid_found = False

    # Se itera sobre cada palabra del arreglo
    for word in palabras:
        try:
            resultado = cuenta(word, palabras, 0, len(palabras) - 1)
            # La condición de la fase es que el valor retornado esté en [401, 799]
            if 401 <= resultado <= 799:
                print(f"Palabra: '{word}'  ->  Cuenta: {resultado}")
                valid_found = True
        except Exception:
            # Si se lanza excepción, esa palabra no cumple con la condición
            pass

    if not valid_found:
        print("No se encontraron palabras que cumplan la condición.")

if __name__ == "__main__":
    main()
