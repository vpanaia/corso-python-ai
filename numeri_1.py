numeri = [5, 12, 26, 30, 20, 9, 14, 209]

# creare una nuova lista solo con i numeri
# maggiori di 10 e divisi per 2

risultato = []

for numero in numeri:
    if numero > 10:
        risultato.append(numero / 2)

print(risultato)