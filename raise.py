from ErroreCustom import ErroreCustom


def dividi(a, b):
    if b == 7:
        raise ErroreCustom("Il 7 non mi piace ti ho detto!")
    return a / b

try:
    print(dividi(1, 7))
except ErroreCustom as e:
    print()