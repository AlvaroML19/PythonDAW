#Escribe potencia(base, exponente) con exponente a 2 por defecto, y comprueba que los parámetros con valor por defecto van al final.

def potencia(base: float, exponente: float = 2):
    return base ** exponente

print(potencia(5))  
print(potencia(5, 3))  