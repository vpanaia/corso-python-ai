nomi = ["anna", "luca", "ciccio"]
nomi_2 = ["Anna", "Ciccio", "Francesca", "Annibale"]
lun = { nome: len(nome) for nome in nomi}

print(lun)

lun_2 = {
    n: "Lungo" if len(n) > 5 else "Corto"
    for n in nomi_2
        }
