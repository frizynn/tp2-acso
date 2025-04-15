def strcompare(a: str, b: str) -> int:
    """
    compares two strings lexicographically.
      returns 0 if they are equal,
      returns a negative value if 'a' is less than 'b',
      returns a positive value if 'a' is greater than 'b'.
    """
    if a == b:
        return 0
    elif a < b:
        return -1
    else:
        return 1

def explode_bomb():
    """simulates the bomb explosion by raising an exception."""
    raise Exception("the bomb has exploded! error in search parameters.")

def cuenta(input_str: str, palabras: list, low: int, high: int) -> int:
    """
    recursive function that implements a binary search similar to the assembly code.
    
    parameters:
      - input_str: input word to search for.
      - palabras: list of words (assumed sorted).
      - low: lower index of the range.
      - high: upper index of the range.
    
    the function calculates the middle index using the formula:
          mid = (low & high) + ((low ^ high) >> 1)
    and then compares `input_str` with the word at that position. if the comparison is 0,
    returns the ascii value of the first character of the found word; otherwise,
    makes recursive calls accumulating that value.
    
    if at any point the range is not valid (e.g., high <= mid or low >= mid),
    the bomb explosion is simulated.
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

    # reads the file "bomb3/palabras.txt"
    try:
        with open("bomb3/palabras.txt", "r", encoding="utf-8") as file:
            # removes empty lines and strips whitespace
            palabras = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print("error: file 'bomb3/palabras.txt' not found.")
        sys.exit(1)

    if not palabras:
        print("error: the word list is empty.")
        sys.exit(1)

    # sorts the list (binary search assumes it is sorted)
    palabras.sort()

    print("searching for words that meet the phase 3 condition:")
    print("the result (value of 'cuenta') must be between 401 and 799.\n")

    valid_found = False

    # iterate over each word in the array
    for word in palabras:
        try:
            resultado = cuenta(word, palabras, 0, len(palabras) - 1)
            # the phase condition is that the returned value is in [401, 799]
            if 401 <= resultado <= 799:
                print(f"word: '{word}'  ->  cuenta: {resultado}")
                valid_found = True
        except Exception:
            # if an exception is raised, that word does not meet the condition
            pass

    if not valid_found:
        print("no words found that meet the condition.")

if __name__ == "__main__":
    main()
