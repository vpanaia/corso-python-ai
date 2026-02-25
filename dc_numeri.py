studente = {
    "nome": "Anna",
    "eta": 22,
    "corso": "Python"
}

num = [10,20,30]
quadrati = {}

for n in num:
    quadrati[n] = n * n

print(quadrati)

"""
{ chiave : valore for elemento in sequenza}
"""

quadrati_c = { n : n * n for n in num }

print(quadrati_c)

numeri = [3,6,9,12,15,18,21,24,27,30]

ris = { n: n/3 for n in numeri}

