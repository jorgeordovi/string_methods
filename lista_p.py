lista = ["Manzana", "Pera", "Banana", "Mandarina","Toronja"]
print(lista[-1])
print(lista[2:5])

lista_mod = ["Manzana", "Pera", "Banana", "Mandarina","Toronja"]
lista_mod[1] = "Puya" 
lista_mod[3] = "Remera"
lista_mod[2] = "Linda"
print(lista_mod)
lista_mods = ["Manzana", "Pera", "Banana", "Mandarina","Toronja"]
lista_mods[5:] = ["Lady", "Pros"]
lista_mods.insert(6, "La")
print(lista_mods)
lista_mod.extend(lista_mods)
print(lista_mod)