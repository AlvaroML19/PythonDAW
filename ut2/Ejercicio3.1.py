#Escribe presentar(nombre, ciudad) y llámala por posición y por nombre.

def presentar(nombre:str, ciudad:str):
    return f"Hola, me llamo {nombre} y soy de {ciudad}"

print (presentar("Grace", "Londres"))
print (presentar(ciudad="Londres", nombre="Grace"))