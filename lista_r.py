lista_mods = ["Manzana", "Pera", "Banana", "Mandarina","Toronja", "Puta", "Lady"]
#lista_mods.pop(2) # Remueve el item 
#print(lista_mods)

#for listas in lista_mods: # Imprime por lista nueva linea
#    print(listas)
#Bucle for con indice disponible  
#for i in range(len.listas):
#    print(lista_mods[i])

#Bucle for con indice i
#for i in range(6):
#   print(lista_mods[i]) 
#   print(i)

#bucle while
#i = 0
#while i < len(lista_mods):
#   print(lista_mods[i])
#   i += 1

#Busqueda en lista por caracter
lista_mods_e = []



for lista in lista_mods:
    if "e" in lista:
        lista_mods_e.append(lista)

print(lista_mods_e)
lista_mods_l = [lista for lista in lista_mods if "L" in lista]
print(lista_mods_l)