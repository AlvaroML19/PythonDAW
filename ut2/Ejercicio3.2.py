#Añade a saludar(nombre, saludo) un valor por defecto para que saludo sea "Hola" si no se indica.

def saludar(nombre:str, saludo:str="Hola"):
    return f"{saludo}, {nombre}"

print (saludar("Grace"))
print (saludar("Alan", "Buenos días"))