romanNumbers = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

def roman(string):
    if not string: # Si la cadena esta vacia
        return 0
    else:
        decimal = romanNumbers[string[0].upper()]
        if len(string) > 1:
            if decimal < romanNumbers[string[1].upper()]:
                return -decimal + roman(string[1:].upper())
    return decimal + roman(string[1:]) # Llama la cadena a partir del 2° caracter
        
print(roman('MMXXIV')) # 2024
