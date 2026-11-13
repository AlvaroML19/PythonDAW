#Escribe la función más pequeña posible que evite repetir el cálculo del IVA en un programa que factura tres artículos.

IVA: int = 21

def con_iva(precio:float):
    return precio (1 + IVA / 100)

print(f"{con_iva(10):.2f}")
print(f"{con_iva(25):.2f}")
print(f"{con_iva(99):.2f}") 