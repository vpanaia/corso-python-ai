def somma(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("somma, a, b must be int")
    return a + b

def differenza(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("somma, a, b must be int")
    return a - b

def prodotto(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("somma, a, b must be int")
    return a * b

def divisione(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("somma, a, b must be int")
    if b == 0:
        raise ZeroDivisionError("il divisore non può essere zero")
    return a / b