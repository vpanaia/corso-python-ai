temperature = [18, 22, 30, 12, 15, 32, 27, 19, 28, 20]

#Creare una nuova lista con le temperature superiori a 20

alte = []

for temp in temperature:
    if temp > 20:
        alte.append(temp)

print(alte)