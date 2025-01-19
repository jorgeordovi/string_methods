texto = "hi MOm"
texo2 = "   bye to bad life   "
text_separate = "Python,Django,Javascript,React"
lista = ["Jorge", "Juan", "Carlos"]

print("capitalize", texto.capitalize()) # converst the first letter ino capital

print("upper:", texto.upper()) # converts hole ext to CAPS
print("lower:", texto.lower()) # Convierte el exto entero en minuscuilas
print(texo2.strip()) # rids spaces space fron and back
print(texo2.replace("bad", "good").replace("bye", "Hi")) # Split etx by items
print("split", text_separate.split(","))
print("join:", ",".join(lista))# Junta los items de una lista en  un string
print("find:", texto.find("hi"))